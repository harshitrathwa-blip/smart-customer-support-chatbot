import os
from dotenv import load_dotenv

# Load local .env file if it exists
load_dotenv()

def get_gemini_api_key():
    """
    Safely retrieves the Gemini API key from Streamlit secrets (if deployed)
    or from local environment variables (if running locally).
    """
    api_key = None
    
    # Try fetching from Streamlit secrets first (for Streamlit Cloud deployment)
    try:
        import streamlit as st
        if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
            api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass
        
    # Fallback to standard environment variables (.env / OS environment)
    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY")
        
    return api_key