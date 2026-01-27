from backend.utils.disease_loader import load_diseases
from backend.utils.symptom_loader import load_symptom_aliases
from backend.core.symptom_normalizer import normalize_symptoms
from backend.core.red_flag_handler import check_red_flags
from backend.core.inference_engine import infer_diseases
from backend.core.confidence_normalizer import normalize_confidence
from backend.core.follow_up_engine import needs_follow_up
from backend.services.openai_input_parser import parse_input
from backend.services.openai_explanation_generator import explain
from backend.models.ml_models.ml_model import DiseaseRanker
from backend.utils.logger import get_logger

logger = get_logger(__name__)

# Load static resources once at startup
DISEASES = load_diseases()
SYMPTOM_ALIASES = load_symptom_aliases()

# ML ranker (assistive only)
ml_ranker = DiseaseRanker()


def diagnose(user_text: str) -> dict:
    """
    Main diagnosis function: parses input, normalizes symptoms, checks red flags, infers diseases, applies ML ranking, and generates explanation.
    """
    logger.debug("Starting diagnosis for input text: %s", user_text)

    try:
        # 1. Parse raw user input
        parsed = parse_input(user_text)
        raw_symptoms = parsed.get("symptoms", [])
        risk_factors = parsed.get("risk_factors", [])
        logger.debug(
            "Parsed input | raw_symptoms=%s, risk_factors=%s",
            raw_symptoms,
            risk_factors,
        )

        # 2. Normalize symptoms
        normalized_symptoms = normalize_symptoms(raw_symptoms, SYMPTOM_ALIASES)
        logger.debug("Normalized symptoms: %s", normalized_symptoms)

        if not normalized_symptoms:
            logger.info("Not enough symptom information to proceed")
            return {
                "urgent": False,
                "message": "Not enough symptom information to proceed.",
                "follow_up_required": True
            }

        # 3. Check red flags
        red_flag_result = check_red_flags(normalized_symptoms, DISEASES)
        if red_flag_result.get("urgent"):
            logger.info(
                "Urgent red flag detected | red_flag=%s",
                red_flag_result["red_flag"]["name"]
            )
            return {
                "urgent": True,
                "alert": "URGENT MEDICAL ATTENTION REQUIRED",
                "red_flag": red_flag_result["red_flag"]["name"],
                "reason": red_flag_result["red_flag"]["reason"],
                "recommended_action": red_flag_result["red_flag"]["action"],
                "disclaimer": (
                    "This system does not provide a medical diagnosis. "
                    "Please seek immediate care from a qualified healthcare professional."
                )
            }

        # 4. Rule-based disease inference
        rule_results = infer_diseases(
            symptoms=normalized_symptoms,
            risk_factors=risk_factors,
            diseases=DISEASES
        )

        if not rule_results:
            logger.info("No matching conditions found with current information")
            return {
                "urgent": False,
                "message": "No matching conditions found with current information.",
                "follow_up_required": True
            }

        # 5. Confidence normalization
        rule_results = normalize_confidence(rule_results)

        # 6. ML-assisted re-ranking (does NOT override rules)
        final_results = ml_ranker.rerank(rule_results)
        final_results = final_results[:3]  # Keep top 3 only

        # 7. Decide if follow-up questions are needed
        follow_up_required = needs_follow_up(final_results)
        logger.debug("Follow-up required: %s", follow_up_required)

        # 8. Generate explanation
        explanation = explain(final_results)

        # 9. Final response
        logger.info(
            "Diagnosis completed | urgent=False, top_results=%s",
            [r["disease"] for r in final_results],
        )

        return {
            "urgent": False,
            "possible_conditions": final_results,
            "follow_up_required": follow_up_required,
            "explanation": explanation,
            "disclaimer": (
                "This is a clinical decision support suggestion, not a diagnosis. "
                "Please consult a qualified healthcare professional."
            )
        }

    except Exception:
        logger.exception("Error during diagnosis process")
        raise