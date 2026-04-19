from groq import Groq
from app.config import GROQ_API_KEY, MODEL_NAME

# ✅ define client globally
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None


def generate_answer(prompt: str, context: list):
    # ✅ now client is accessible
    if client is None:
        return "Groq API key not configured."

    context_str = "\n".join(context)

    system_prompt = f"""You are a helpful telecom tutor.
Use the following context to answer the user's question accurately.

Context:
{context_str}
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        print("Groq Error:", e)
        return "Error generating response."