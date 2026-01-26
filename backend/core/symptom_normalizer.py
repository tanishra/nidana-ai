from utils.logger import get_logger

logger = get_logger(__name__)


def normalize_symptoms(raw_symptoms, alias_map):
    """
    Normalize raw symptom names to their canonical forms using an alias map.
    """
    logger.debug(
        "Starting symptom normalization | raw_count=%d",
        len(raw_symptoms),
    )

    normalized = set()

    try:
        for symptom in raw_symptoms:
            s = symptom.lower()

            for canonical, aliases in alias_map.items():
                if s in (a.lower() for a in aliases):
                    logger.debug(
                        "Normalized symptom '%s' -> '%s'",
                        symptom,
                        canonical,
                    )
                    normalized.add(canonical)

        logger.info(
            "Symptom normalization completed | normalized_count=%d",
            len(normalized),
        )

        return list(normalized)

    except Exception:
        logger.exception("Error during symptom normalization")
        raise