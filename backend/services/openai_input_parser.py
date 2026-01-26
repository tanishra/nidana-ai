import openai
import os
from utils.logger import get_logger
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_input(text):
    """
    Parse user input using OpenAI to extract symptoms.
    """
    logger.debug("Parsing input text: %s", text)

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Extract symptoms only."},
                {"role": "user", "content": text}
            ]
        )

        symptoms = response.choices[0].message.content.lower().split(",")
        logger.info("Extracted symptoms: %s", symptoms)
        return symptoms

    except Exception:
        logger.exception("Failed to parse input via OpenAI")
        raise