from utils.logger import get_logger

logger = get_logger(__name__)


def check_red_flags(symptoms, diseases):
    """
    Check if any symptoms match disease red flags.
    """
    logger.debug("Checking red flags for symptoms: %s", symptoms)

    try:
        for disease in diseases:
            for flag in disease.get("red_flags", []):
                if flag["name"] in symptoms:
                    logger.info(
                        "Red flag detected | symptom=%s, disease=%s",
                        flag["name"],
                        disease["disease_name"],
                    )
                    return {
                        "urgent": True,
                        "red_flag": flag,
                        "disease": disease["disease_name"],
                    }

        logger.debug("No red flags detected")
        return {"urgent": False}

    except Exception:
        logger.exception("Error while checking red flags")
        raise