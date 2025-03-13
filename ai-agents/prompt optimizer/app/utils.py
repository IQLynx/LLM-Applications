import google.generativeai as genai

def configure_gemini_api(api_key):
    """Configure the Gemini API with the provided API key."""
    if api_key:
        genai.configure(api_key=api_key)
        return True
    else:
        return False