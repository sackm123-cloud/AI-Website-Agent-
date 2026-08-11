import os

from google import genai
from dotenv import load_dotenv

load_dotenv()


MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash",
)


def get_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured"
        )

    return genai.Client(api_key=api_key)


def generate(
    prompt: str,
    system_instruction: str = None,
):
    client = get_client()

    full_prompt = prompt

    if system_instruction:
        full_prompt = (
            f"{system_instruction}\n\n"
            f"USER TASK:\n{prompt}"
        )

    response = client.models.generate_content(
        model=MODEL,
        contents=full_prompt,
    )

    text = getattr(response, "text", None)

    if not text:
        raise RuntimeError(
            "Gemini returned an empty response"
        )

    return text.strip()
