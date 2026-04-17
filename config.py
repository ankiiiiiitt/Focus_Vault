import os
from groq import Groq
from dotenv import load_dotenv

# Ensure .env is loaded from the same directory as this file
base_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(base_dir, ".env"))

api_key = os.getenv("GROQ_API_KEY")

# DEBUG: Print key status for Vercel logs (don't print full key for security)
if api_key:
    print(f"GROQ_API_KEY found: {api_key[:5]}...{api_key[-5:]}")
else:
    print("GROQ_API_KEY is None")

if not api_key:

    # Fallback: check for GROK_API_KEY just in case
    api_key = os.getenv("GROK_API_KEY")

if not api_key:
    print("WARNING: GROQ_API_KEY is missing from environment variables.")
    # We'll initialize with an empty string or dummy to avoid crashes, 
    # but the API calls will fail with a clear error.
    client = Groq(api_key="MISSING")
else:
    client = Groq(api_key=api_key)

