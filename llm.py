import os
from groq import Groq


def format_text_with_llm(raw_text: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return "❌ GROQ_API_KEY not found. Restart terminal."

    client = Groq(api_key=api_key)

    prompt = f"""
You are given OCR-extracted text.

TASK:
- Fix spacing, punctuation, and line breaks
- Correct obvious OCR mistakes
- DO NOT add new information
- DO NOT remove information
- DO NOT summarize or explain
- Preserve meaning exactly

Return ONLY the cleaned text.

OCR TEXT:
{raw_text}
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()
