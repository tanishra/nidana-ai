import json
from pathlib import Path
from backend.utils.logger import get_logger

DATA_PATH = Path("backend/feedback/data")
logger = get_logger(__name__)


def evaluate():
    logger.debug("Starting feedback evaluation from %s", DATA_PATH)

    files = DATA_PATH.glob("*.json")

    total = 0
    top3_hits = 0
    poor_rankings = 0
    overconfidence = 0
    misses = 0

    for f in files:
        try:
            with open(f, "r", encoding="utf-8") as file:
                data = json.load(file)
            total += 1

            if data["accepted_condition"] in data["ai_suggestions"][:3]:
                top3_hits += 1

            if data["ranking_quality"] == "poor":
                poor_rankings += 1

            if data["overconfident"]:
                overconfidence += 1

            if data["missed_condition"]:
                misses += 1
        except Exception:
            logger.exception("Failed to process feedback file: %s", f)

    logger.info(
        "Feedback evaluation completed | cases=%d, top3_hits=%d, poor_rankings=%d, "
        "overconfidence=%d, misses=%d",
        total, top3_hits, poor_rankings, overconfidence, misses
    )

    return {
        "cases": total,
        "top3_acceptance_rate": top3_hits / total if total else 0,
        "poor_ranking_rate": poor_rankings / total if total else 0,
        "overconfidence_rate": overconfidence / total if total else 0,
        "miss_rate": misses / total if total else 0
    }