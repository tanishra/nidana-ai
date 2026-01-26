from utils.logger import get_logger

logger = get_logger(__name__)


def needs_follow_up(results):
    """
    Determine if a follow-up is needed based on top disease inference results.
    """
    logger.debug("Checking if follow-up is needed | results=%s", results)

    try:
        if len(results) < 2:
            logger.debug("Less than two results, follow-up not needed")
            return False

        diff = abs(results[0]["score"] - results[1]["score"])
        logger.debug(
            "Score difference between top two results: %d", diff
        )

        follow_up_needed = diff < 3
        logger.info("Follow-up needed: %s", follow_up_needed)
        return follow_up_needed

    except Exception:
        logger.exception("Error while evaluating follow-up requirement")
        raise