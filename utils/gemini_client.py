import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def generate_email(prompt: str) -> str:
    """
    Generate an email using Gemini.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API key not found.")

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        if (
            response is None
            or response.text is None
            or not response.text.strip()
        ):
            raise ValueError("Gemini returned an empty response.")

        return response.text.strip()

    except Exception as error:
        raise ValueError(f"Gemini API Error: {error}")