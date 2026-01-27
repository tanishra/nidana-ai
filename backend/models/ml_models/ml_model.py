from typing import List, Dict
import numpy as np
import joblib
from pathlib import Path
from backend.utils.logger import get_logger

logger = get_logger(__name__)

MODEL_PATH = Path("backend/ml/production_ranker.joblib")


class ProductionDiseaseRanker:
    """
    Production-grade ML ranker.

    Role:
    - Assist rule-based inference
    - Improve ranking stability
    - NEVER override safety or red-flag logic
    """

    def __init__(self):
        if not MODEL_PATH.exists():
            logger.error(
                "ML model not found at %s. Train and export production_ranker.joblib",
                MODEL_PATH
            )
            raise RuntimeError(
                "ML model not found. Train and export production_ranker.joblib"
            )
        self.model = joblib.load(MODEL_PATH)
        logger.info("Loaded ML model from %s", MODEL_PATH)

    # -----------------------------
    # Feature Engineering (Critical)
    # -----------------------------
    def _extract_features(self, result: Dict) -> np.ndarray:
        """
        Convert rule-engine output into ML-safe features.
        """
        confidence = result.get("confidence", 0.0)
        score = result.get("score", 0)
        matched_symptoms = len(result.get("matched_symptoms", []))
        total_symptoms = max(matched_symptoms, 1)
        key_symptom_ratio = result.get("key_symptom_ratio", 0.0)

        features = np.array([
            confidence / 100.0,          # normalized confidence
            score / 50.0,                # bounded score scale
            matched_symptoms / 10.0,     # symptom coverage
            key_symptom_ratio            # clinical specificity
        ])
        logger.debug("Extracted features for result %s: %s", result.get("disease"), features)
        return features.reshape(1, -1)

    # -----------------------------
    # Re-ranking Logic
    # -----------------------------
    def rerank(self, rule_results: List[Dict]) -> List[Dict]:
        """
        ML-assisted re-ranking.
        Safe, bounded, explainable.
        """
        if not rule_results:
            logger.debug("No rule_results provided to rerank")
            return rule_results

        enriched_results = []

        for r in rule_results:
            features = self._extract_features(r)
            adjustment = float(self.model.predict(features)[0])
            logger.debug(
                "Predicted ML adjustment for %s: %f", r.get("disease"), adjustment
            )

            # HARD BOUNDS (Safety)
            adjustment = max(min(adjustment, 10.0), -10.0)
            final_score = r["confidence"] + adjustment

            enriched = {
                **r,
                "ml_adjustment": round(adjustment, 2),
                "final_confidence": round(final_score, 2)
            }
            logger.debug(
                "Enriched result for %s: %s", r.get("disease"), enriched
            )

            enriched_results.append(enriched)

        # Sort by ML-adjusted confidence
        enriched_results.sort(
            key=lambda x: x["final_confidence"],
            reverse=True
        )
        logger.info("Completed ML-assisted reranking")
        return enriched_results