import openai
import os
from backend.utils.logger import get_logger
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")


def explain(results):
    """
    Use OpenAI to generate a simple explanation of inference results.
    """
    logger.debug("Explaining results: %s", results)

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Explain reasoning simply."},
                {"role": "user", "content": str(results)}
            ]
        )

        explanation = response.choices[0].message.content
        logger.info("Generated explanation successfully")
        return explanation

    except Exception:
        logger.exception("Failed to generate explanation via OpenAI")
        raise