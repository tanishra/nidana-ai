from backend.utils.disease_loader import load_diseases
from backend.utils.symptom_loader import load_symptom_aliases
from backend.core.symptom_normalizer import normalize_symptoms
from backend.core.red_flag_handler import check_red_flags
from backend.core.inference_engine import infer_diseases
from backend.services.openai_input_parser import parse_input
from backend.services.openai_explanation_generator import explain
from utils.logger import get_logger

logger = get_logger(__name__)

diseases = load_diseases()
aliases = load_symptom_aliases()


def diagnose(text):
    """
    Main diagnosis function: parses input, normalizes symptoms, checks red flags, infers diseases, and generates explanation.
    """
    logger.debug("Starting diagnosis for input text: %s", text)

    try:
        raw_symptoms = parse_input(text)
        logger.debug("Raw symptoms extracted: %s", raw_symptoms)

        symptoms = normalize_symptoms(raw_symptoms, aliases)
        logger.debug("Normalized symptoms: %s", symptoms)

        red_flag = check_red_flags(symptoms, diseases)
        if red_flag["urgent"]:
            logger.info(
                "Urgent red flag detected | symptom=%s, disease=%s",
                red_flag["red_flag"]["name"],
                red_flag["disease"],
            )
            return {"urgent": True, "details": red_flag}

        results = infer_diseases(symptoms, [], diseases)
        explanation = explain(results)

        logger.info(
            "Diagnosis completed | urgent=False, top_results=%s",
            [r["disease"] for r in results],
        )

        return {
            "urgent": False,
            "results": results,
            "explanation": explanation
        }

    except Exception:
        logger.exception("Error during diagnosis process")
        raise