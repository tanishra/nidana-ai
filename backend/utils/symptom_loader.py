import json

from utils.logger import get_logger

logger = get_logger(__name__)


def load_symptom_aliases(
    path: str = "backend/knowledge_base/symptoms/symptom_aliases.json",
):
    """
    Load symptom aliases from the knowledge base.
    """
    try:
        logger.debug("Loading symptom aliases from %s", path)

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        logger.info("Successfully loaded symptom aliases")

        return data

    except Exception:
        logger.exception("Failed to load symptom aliases")
        raise