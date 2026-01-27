import json
import numpy as np
import joblib
from pathlib import Path
from sklearn.ensemble import GradientBoostingRegressor
from backend.utils.logger import get_logger

logger = get_logger(__name__)

FEEDBACK_PATH = Path("backend/feedback/data")
MODEL_PATH = Path("backend/models/ml_models/disease_ranker.joblib")


def train():
    X = []
    y = []

    logger.info("Starting ML retraining from doctor feedback")

    for f in FEEDBACK_PATH.glob("*.json"):
        with open(f, "r") as file:
            data = json.load(file)

        # Features (from rule engine output)
        avg_conf = sum(data["ai_confidences"]) / len(data["ai_confidences"])

        # Target adjustment
        if data["ranking_quality"] == "good":
            adjustment = 0
        elif data["ranking_quality"] == "acceptable":
            adjustment = -2
        else:
            adjustment = -5

        X.append([avg_conf / 100])
        y.append(adjustment)

        logger.debug(
            "Processed feedback file %s | avg_conf=%.2f | adjustment=%d",
            f.name, avg_conf, adjustment
        )

    model = GradientBoostingRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=3,
        random_state=42
    )

    model.fit(np.array(X), np.array(y))
    joblib.dump(model, MODEL_PATH)

    logger.info("✅ Model retrained from doctor feedback and saved to %s", MODEL_PATH)


if __name__ == "__main__":
    train()