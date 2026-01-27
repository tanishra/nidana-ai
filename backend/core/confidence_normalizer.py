from backend.utils.logger import get_logger

logger = get_logger(__name__)

def normalize_confidence(results):
    logger.debug("Normalizing confidence for results: %s", results)

    if not results:
        logger.debug("No results provided, returning as-is")
        return results

    max_score = results[0]["score"]
    logger.debug("Max score detected: %s", max_score)

    if max_score == 0:
        logger.debug("Max score is 0, skipping normalization")
        return results

    for r in results:
        r["confidence"] = round((r["score"] / max_score) * 100, 2)
        logger.debug(
            "Normalized score %s to confidence %s",
            r["score"],
            r["confidence"]
        )

    logger.info("Confidence normalization completed")
    return results