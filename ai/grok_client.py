from openai import OpenAI
from dotenv import load_dotenv
import os

# ============================================
# Load Environment Variables
# ============================================

load_dotenv()

# ============================================
# Read API Key
# ============================================

api_key = os.getenv("GROQ_API_KEY")

# ============================================
# Create OpenAI-Compatible Client for Groq
# ============================================

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)


# ============================================
# Ask Groq
# ============================================

def ask_grok(prompt):

    try:

        response = client.chat.completions.create(

            model="openai/gpt-oss-20b",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI Maternal Health Assistant. "
                        "Provide educational information only. "
                        "Do not diagnose diseases or prescribe medication. "
                        "Always encourage users to consult qualified healthcare professionals "
                        "for medical concerns."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3,

            max_tokens=700
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"""
⚠️ **AI Assistant Temporarily Unavailable**

The Machine Learning prediction was completed successfully, but the AI explanation could not be generated.

**Possible reasons:**
- No internet connection
- Invalid or expired API key
- Groq service is temporarily unavailable
- API rate limit reached

**Technical details:**
{str(e)}

Please try again in a few moments.
"""
