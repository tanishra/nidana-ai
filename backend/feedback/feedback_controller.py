from fastapi import APIRouter
from backend.feedback.schemas import DoctorFeedback
import json
from pathlib import Path
from backend.utils.logger import get_logger

router = APIRouter()
FEEDBACK_STORE = Path("backend/feedback/data")
FEEDBACK_STORE.mkdir(parents=True, exist_ok=True)

logger = get_logger(__name__)


@router.post("/feedback")
def submit_feedback(feedback: DoctorFeedback):
    file_path = FEEDBACK_STORE / f"{feedback.case_id}.json"
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(feedback.dict(), f, indent=2, default=str)
        logger.info("Feedback saved successfully | case_id=%s", feedback.case_id)
        return {"status": "feedback_saved"}
    except Exception:
        logger.exception("Failed to save feedback | case_id=%s", feedback.case_id)
        raise