from backend.utils.logger import get_logger

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
            matched_common = []
            matched_key = []
            matched_risk = []

            # Check common symptoms
            for s in disease.get("common_symptoms", []):
                if s["name"] in symptoms:
                    matched_common.append(s["name"])

            # Check key symptoms
            for s in disease.get("key_symptoms", []):
                if s["name"] in symptoms:
                    matched_key.append(s["name"])

            # Check risk factors
            for r in disease.get("risk_factors", []):
                if r["name"] in risk_factors:
                    matched_risk.append(r["name"])

            total_matched = len(matched_common) + len(matched_key)

            if total_matched == 0:
                continue

            # Calculate score (same as previous logic)
            score = sum(s["weight"] for s in disease.get("common_symptoms", []) if s["name"] in matched_common)
            score += sum(s["weight"] * 2 for s in disease.get("key_symptoms", []) if s["name"] in matched_key)
            score += 2 * len(matched_risk)

            result = {
                "disease": disease["disease_name"],
                "score": score,
                "matched_common": matched_common,
                "matched_key": matched_key,
                "matched_risk": matched_risk,
                "total_common": len(disease.get("common_symptoms", [])),
                "total_key": len(disease.get("key_symptoms", []))
            }
            results.append(result)

            logger.debug(
                "Disease matched | disease=%s, score=%d, matched_common=%s, matched_key=%s, matched_risk=%s",
                disease["disease_name"],
                score,
                matched_common,
                matched_key,
                matched_risk,
            )

        sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)
        logger.info(
            "Disease inference completed | diseases=%s",
            [r["disease"] for r in sorted_results],
        )
        return sorted_results

    except Exception:
        logger.exception("Error during disease inference")
        raise