import json
from pathlib import Path

from utils.logger import get_logger

logger = get_logger(__name__)

DISEASE_PATH = Path("backend/knowledge_base/diseases")


def load_diseases():
    """
    Load all disease JSON files from the knowledge base.
    """
    diseases = []

    try:
        for file in DISEASE_PATH.glob("*.json"):
            logger.debug("Loading disease file: %s", file.name)

            with open(file, "r", encoding="utf-8") as f:
                diseases.append(json.load(f))

        logger.info("Successfully loaded %d disease records", len(diseases))

    except Exception:
        logger.exception("Error while loading disease data")
        raise

    return diseases