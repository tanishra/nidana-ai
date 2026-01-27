import openai
import os
from backend.utils.logger import get_logger
from dotenv import load_dotenv
import json

load_dotenv()

logger = get_logger(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """
You are a medical language parser.
Your task is ONLY to extract symptoms explicitly mentioned in the text.
DO NOT diagnose diseases.
DO NOT suggest conditions.
DO NOT add medical reasoning.
Return STRICT JSON only in the following format:
{ "symptoms": ["symptom1", "symptom2"], "risk_factors": ["risk1", "risk2"] }
"""

USER_PROMPT_TEMPLATE = """
Extract symptoms and risk factors from the following text.

Text:
\"\"\"{text}\"\"\"

Return JSON ONLY.
"""

def parse_input(text):
    """
    Parse user input using OpenAI to extract symptoms and risk factors.
    """
    logger.debug("Parsing input text: %s", text)

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT_TEMPLATE.format(text=text)}
            ]
        )

        content = response.choices[0].message.content.strip()
        data = json.loads(content)

        symptoms = [s.lower() for s in data.get("symptoms", [])]
        risk_factors = [r.lower() for r in data.get("risk_factors", [])]

        logger.info("Extracted symptoms: %s", symptoms)
        logger.info("Extracted risk factors: %s", risk_factors)

        return {
            "symptoms": symptoms,
            "risk_factors": risk_factors
        }

    except Exception:
        logger.exception("Failed to parse input via OpenAI")
        raise