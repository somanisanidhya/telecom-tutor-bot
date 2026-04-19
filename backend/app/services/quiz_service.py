import json
from groq import Groq
from app.config import GROQ_API_KEY, MODEL_NAME
from app.db.data_loader import telecom_chunks
import random

client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

def generate_quiz(topic: str = "telecommunications", questions_count: int = 3):
    if not client:
        return []

    # get some random context
    context_samples = random.sample(telecom_chunks, min(len(telecom_chunks), 5))
    context_str = "\n".join(context_samples)

    system_prompt = f"""You are a telecom tutor creating a quiz based on the provided context.
Generate {questions_count} multiple-choice questions about {topic}.
Return ONLY a valid JSON array matching the exact structure below. Output no markdown padding, no code blocks, just raw JSON text.

Structure:
[
  {{
    "id": "q1",
    "question": "question text",
    "options": [
      {{"id": "a", "text": "option A text"}},
      {{"id": "b", "text": "option B text"}},
      {{"id": "c", "text": "option C text"}},
      {{"id": "d", "text": "option D text"}}
    ],
    "correct_option_id": "a"
  }}
]

Context:
{context_str}
"""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": "Generate the quiz in requested JSON format."}
            ]
        )
        content = response.choices[0].message.content.strip()
        if content.startswith("```json"):
            content = content[7:-3]
        elif content.startswith("```"):
            content = content[3:-3]
            
        quiz_data = json.loads(content)
        return quiz_data
    except Exception as e:
        print(f"Quiz generation error: {e}")
        return []
