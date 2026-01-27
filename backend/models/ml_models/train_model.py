import numpy as np
import joblib
from pathlib import Path
from sklearn.ensemble import GradientBoostingRegressor

MODEL_PATH = Path("backend/models/ml_models/disease_ranker.joblib")

def generate_synthetic_training_data():
    """
    Bootstrap training data.
    This simulates how rule-engine outputs should be nudged.
    """

    X = []
    y = []

    # confidence, score, matched_symptoms, key_symptom_ratio
    samples = [
        (90, 25, 6, 0.8, 5),
        (85, 22, 5, 0.7, 4),
        (70, 18, 4, 0.6, 2),
        (60, 15, 3, 0.4, 0),
        (50, 12, 2, 0.3, -1),
        (40, 8, 2, 0.2, -3),
        (30, 6, 1, 0.1, -5),
    ]

    for conf, score, sym_cnt, key_ratio, adj in samples:
        X.append([
            conf / 100.0,
            score / 50.0,
            sym_cnt / 10.0,
            key_ratio
        ])
        y.append(adj)

    return np.array(X), np.array(y)


def train_and_save():
    X, y = generate_synthetic_training_data()

    model = GradientBoostingRegressor(
        n_estimators=150,
        learning_rate=0.05,
        max_depth=3,
        random_state=42
    )

    model.fit(X, y)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print("✅ disease_ranker.joblib created successfully")


if __name__ == "__main__":
    train_and_save()