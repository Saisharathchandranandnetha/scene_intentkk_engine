from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

RISK_MODEL = "llama-3.1-8b-instant"

def analyze_scene_risk(scene_text: str) -> dict:
    prompt = f"""
You are a film production safety and feasibility expert.

Analyze the following script scene from a production perspective.
Use reasoning, not keyword matching.

Identify risks related to:
- Crowd management
- Night shoots
- Weather dependency
- Physical stunts
- Visual effects complexity

For each detected risk:
- Explain why it is risky
- Assess severity realistically

Then provide:
- Overall risk level: Low / Medium / High
- Clear justification
- Practical mitigation suggestions

Return ONLY valid JSON.
No markdown. No extra commentary.

JSON format:
{{
  "overall_risk_level": "Low/Medium/High",
  "detected_risks": [
    {{
      "factor": "Risk Factor Name",
      "severity": "Low/Medium/High",
      "reason": "Explanation"
    }}
  ],
  "justification": "Overall reasoning",
  "mitigation_suggestions": ["Suggestion 1", "Suggestion 2"],
  "confidence": 0.0
}}

Scene:
\"\"\"{scene_text}\"\"\"
"""

    try:
        response = client.chat.completions.create(
            model=RISK_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=800
        )
        
        content = response.choices[0].message.content
        # Basic cleanup for JSON
        content = content.replace("```json", "").replace("```", "").strip()
        return json.loads(content)
    except Exception as e:
        return {
            "overall_risk_level": "Unknown",
            "detected_risks": [],
            "justification": f"Error analyzing risk: {str(e)}",
            "mitigation_suggestions": [],
            "confidence": 0.0
        }
