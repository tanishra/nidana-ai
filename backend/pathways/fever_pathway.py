from typing import List, Dict
from backend.utils.logger import get_logger
from backend.core.inference_engine import infer_diseases
from backend.core.confidence_normalizer import normalize_confidence
from backend.core.red_flag_handler import check_red_flags

logger = get_logger(__name__)


class FeverPathway:
    """
    Fever Pathway Engine

    Handles clinical reasoning for patients presenting with fever.
    Focuses on safety, conservative inference, and clinically realistic outputs.
    """

    PATHWAY_NAME = "fever"

    def __init__(self, diseases: List[Dict]):
        """
        diseases: full disease knowledge base (list of disease dicts)
        """
        self.diseases = diseases
        self.fever_diseases = self._filter_fever_diseases(diseases)

        logger.info(
            "FeverPathway initialized with %d fever-related diseases",
            len(self.fever_diseases)
        )

    # Internal helpers
    def _filter_fever_diseases(self, diseases: List[Dict]) -> List[Dict]:
        """
        Select only diseases relevant to fever pathway.
        """
        fever_related = []

        for d in diseases:
            pathways = d.get("pathways", [])
            if self.PATHWAY_NAME in pathways:
                fever_related.append(d)

        return fever_related

    # Public API
    def run(
        self,
        normalized_symptoms: List[str],
        risk_factors: List[str] = None
    ) -> Dict:
        """
        Execute fever pathway reasoning.
        """

        risk_factors = risk_factors or []

        logger.info(
            "Running FeverPathway | symptoms=%s | risk_factors=%s",
            normalized_symptoms,
            risk_factors
        )

        # Step 1: Safety first (Red Flags)
        red_flag_result = check_red_flags(
            symptoms=normalized_symptoms,
            diseases=self.fever_diseases
        )

        if red_flag_result:
            logger.warning(
                "Red flag detected in FeverPathway: %s",
                red_flag_result
            )
            return red_flag_result

        # Step 2: Core inference
        raw_results = infer_diseases(
            symptoms=normalized_symptoms,
            risk_factors=risk_factors,
            diseases=self.fever_diseases
        )

        if not raw_results:
            logger.info("No fever-related diseases matched")
            return {
                "possible_conditions": [],
                "follow_up_required": True,
                "explanation": (
                    "Fever is present, but there are insufficient distinguishing "
                    "features to suggest a specific cause at this time. "
                    "Additional symptoms, duration, or investigations may help."
                )
            }

        # Step 3: Confidence normalization
        ranked_results = normalize_confidence(raw_results)

        # Step 4: Prepare output
        logger.info(
            "FeverPathway completed with %d ranked conditions",
            len(ranked_results)
        )

        return {
            "possible_conditions": ranked_results[:3],
            "follow_up_required": any(
                r["confidence"] < 40 for r in ranked_results[:3]
            ),
            "pathway": self.PATHWAY_NAME
        }