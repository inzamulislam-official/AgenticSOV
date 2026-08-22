import json

from app.llm.ollama_client import query_ollama


def analyze_brand_response(brand: str, response: str) -> dict:

    prompt = f"""
Analyze the following AI-generated answer.

Brand: {brand}

Determine:

1. Was the brand mentioned?
2. Was the brand recommended?
3. Was the brand described positively, negatively, or neutrally?

Return ONLY valid JSON:

{{
  "mentioned": true,
  "recommended": true,
  "sentiment": "positive"
}}

Answer:

{response}
"""

    result = query_ollama(prompt)

    try:
        return json.loads(result)

    except json.JSONDecodeError:
        return {
            "mentioned": False,
            "recommended": False,
            "sentiment": "unknown"
        }