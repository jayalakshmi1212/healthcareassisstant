import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_json_from_note(note: str):
    prompt = f"""
    Convert the following doctor's note into structured JSON:

    Note: {note}

    Format:
    {{
      "symptoms": [...],
      "duration": "...",
      "sugar_level_status": "...",
      "allergies": "...",
      "prescription": [...]
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a medical assistant that extracts structured data."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    content = response.choices[0].message.content

   
    content = content.strip("` \n")
    content = content.replace("json", "", 1).strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {"error": "Failed to parse GPT response", "raw": content}