from ai_modules.scene_risk_analyzer import analyze_scene_risk
import json

scene_text = """
EXT. MARKET CHASE - NIGHT
A densely packed crowd pushes through the narrow streets. Flares illuminate the sky.
Ravi jumps from a rooftop, landing on a moving truck. The crowd screams as he slides off.
"""

print("Analyzing scene risk...")
result = analyze_scene_risk(scene_text)
print(json.dumps(result, indent=2))
