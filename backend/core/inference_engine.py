from utils.logger import get_logger

logger = get_logger(__name__)


def infer_diseases(symptoms, risk_factors, diseases):
    """
    Infer possible diseases based on symptoms and risk factors.
    """
    logger.debug(
        "Starting disease inference | symptoms=%s, risk_factors=%s",
        symptoms,
        risk_factors,
    )

    try:
        results = []

        for disease in diseases:
            score = 0
            matched = []

            for s in disease.get("common_symptoms", []):
                if s["name"] in symptoms:
                    score += s["weight"]
                    matched.append(s["name"])

            for s in disease.get("key_symptoms", []):
                if s["name"] in symptoms:
                    score += s["weight"] * 2
                    matched.append(s["name"])

            for r in disease.get("risk_factors", []):
                if r["name"] in risk_factors:
                    score += 2

            if score > 0:
                results.append({
                    "disease": disease["disease_name"],
                    "score": score,
                    "matched_symptoms": matched
                })
                logger.debug(
                    "Disease matched | disease=%s, score=%d, matched_symptoms=%s",
                    disease["disease_name"],
                    score,
                    matched,
                )

        top_results = sorted(results, key=lambda x: x["score"], reverse=True)[:3]
        logger.info(
            "Disease inference completed | top_results=%s",
            [r["disease"] for r in top_results],
        )
        return top_results

    except Exception:
        logger.exception("Error during disease inference")
        raise