import json
from pathlib import Path
from backend.feedback.schemas import DoctorFeedback
from backend.utils.logger import get_logger

logger = get_logger(__name__)

FEEDBACK_DIR = Path("backend/feedback/data")
FEEDBACK_DIR.mkdir(parents=True, exist_ok=True)


def save_feedback(feedback: DoctorFeedback):
    file_path = FEEDBACK_DIR / f"{feedback.case_id}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(feedback.dict(), f, indent=2, default=str)

    logger.info("Saved doctor feedback | case_id=%s | path=%s", feedback.case_id, file_path)