import openai
import os
from backend.utils.logger import get_logger
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")


SYSTEM_PROMPT = """
You are a clinical decision-support explanation assistant.

Your job is to generate explanations that doctors trust.

Rules you MUST follow:
- Do NOT diagnose.
- Do NOT claim certainty.
- Do NOT repeat raw scores mechanically.
- Explain clinical reasoning in plain medical language.
- Clearly state why confidence is LOW, MODERATE, or HIGH.
- Explain what evidence is missing.
- Mention why diseases are considered, not confirmed.
- Explain why other plausible diseases were not considered top candidates.
- Write like a clinician explaining to another clinician.
- Provide actionable suggestions for follow-up history or exams.
"""


def explain(results):
    """
    Generate a clinically sound, doctor-acceptable explanation
    for ranked disease possibilities.
    """

    logger.debug("Explaining results: %s", results)

    if not results:
        return (
            "No sufficient clinical evidence is available to suggest "
            "specific conditions at this time. More symptom details are required."
        )

    # Prepare structured context for the LLM
    structured_context = []

    for r in results:
        structured_context.append({
            "disease": r.get("disease"),
            "confidence": r.get("final_confidence", r.get("confidence")),
            "matched_common_symptoms": r.get("matched_common", []),
            "matched_key_symptoms": r.get("matched_key", []),
            "matched_risk_factors": r.get("matched_risk", []),
            "total_common_symptoms": r.get("total_common", 0),
            "total_key_symptoms": r.get("total_key", 0),
        })

    USER_PROMPT = f"""
You are given ranked possible medical conditions with supporting evidence.

Requirements for explanation:
- Write a short, concise summary for each condition (3–5 sentences max)
- Explain why the disease is being considered and its confidence (LOW, MODERATE, HIGH)
- Mention key matched symptoms, key symptoms, and risk factors
- Clearly state missing information
- Explain briefly why other plausible conditions were not ranked higher
- Suggest follow-up history, labs, or exams if needed
- Avoid long narratives; doctors should grasp it quickly

Data:
{structured_context}

Output:
- Concise clinical narrative per condition
- No bullet points
- End by indicating if more information is needed
"""

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.2,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT}
            ]
        )

        explanation = response.choices[0].message.content.strip()
        logger.info("Generated clinical explanation successfully")
        return explanation

    except Exception:
        logger.exception("Failed to generate explanation via OpenAI")
        raise