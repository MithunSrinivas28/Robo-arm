# robotic-arm/intent_parser.py
import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load Gemini API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not set in environment")
# Configure Gemini (google-generativeai client)
genai.configure(api_key=api_key)

def parse_intent(command):
    """
    Use Google Gemini to parse a natural language command into intent.
    Returns a dict with keys 'action', 'color', 'object'.
    """
    prompt = f"Command: '{command}'. Provide output as JSON with keys 'action', 'color', 'object'."
    response = genai.chat(messages=prompt)
    text = response.last.strip()
    try:
        # Attempt to parse JSON from response
        intent = json.loads(text)
    except Exception:
        # Fallback: simple key:value parsing if JSON failed
        try:
            pairs = [part.split(':') for part in text.split(',')]
            intent = {k.strip(): v.strip() for (k, v) in pairs if len(v.strip())>0}
        except Exception:
            intent = {}
    return intent
