from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class DoctorFeedback(BaseModel):
    case_id: str

    # Input snapshot
    presented_symptoms: List[str]

    # AI output snapshot
    ai_suggestions: List[str]
    ai_confidences: List[float]

    # Doctor judgment
    accepted_condition: Optional[str] = None
    ranking_quality: str  # "good" | "acceptable" | "poor"

    missed_condition: Optional[str] = None
    overconfident: bool = False
    underconfident: bool = False

    feedback_notes: Optional[str] = None

    created_at: datetime