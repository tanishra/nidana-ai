from pydantic import BaseModel

class DiagnosisRequest(BaseModel):
    text: str

class DiagnosisResponse(BaseModel):
    result: dict