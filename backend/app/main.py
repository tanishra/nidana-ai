from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.schemas import DiagnosisRequest
from backend.app.diagnosis_controller import diagnose
from backend.utils.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(title="Clinical Decision Support API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/diagnose")
def diagnose_api(req: DiagnosisRequest):
    logger.debug("Received /diagnose request | text=%s", req.text)
    try:
        response = diagnose(req.text)
        logger.info(
            "Diagnosis API response | urgent=%s, results_count=%d",
            response.get("urgent"),
            len(response.get("results", []))
        )
        return response
    except Exception:
        logger.exception("Error handling /diagnose request")
        raise