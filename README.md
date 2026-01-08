🎬 Scene Intent & Visual Planning Engine (SceneSense AI)

Hackathon Project
Transform raw film script scenes into actionable cinematic intent using LLM-based reasoning.

🚀 Problem Statement

Film directors, cinematographers, and writers often start with unstructured script text.
Converting that text into emotion, mood, camera direction, and visual planning takes time, experience, and multiple creative iterations.

There is no lightweight tool that:

Reads a scene like a human filmmaker

Extracts creative intent

Outputs production-ready guidance

💡 Solution

SceneSense AI is a pre-production assistant that:

Analyzes a single screenplay scene

Infers emotion, narrative purpose, visual mood, and camera style

Returns structured JSON that can be directly used for:

Storyboarding

Shot planning

Lighting & mood decisions

Creative review prioritization

All in seconds, using LLM-based reasoning.

✨ Key Features

🎭 Emotion Detection – primary emotional tone of the scene

🧠 Narrative Intent – why the scene exists in the story

🎥 Camera Style Suggestions – framing & movement ideas

🌗 Visual Mood – lighting & atmosphere guidance

📊 Confidence Score – how strongly the intent is inferred

⚡ Real-time Analysis via Groq LLMs

🖥️ Clean Streamlit UI (no setup for users)

🛠️ Tech Stack

Frontend / App: Streamlit

LLM Inference: Groq API

Model Used: llama-3.1-8b-instant

Language: Python

Secrets Management: .env + .gitignore

🧪 Example Input
INT. ABANDONED WAREHOUSE – NIGHT

John pauses before answering. His jaw tightens.
Rain echoes on the metal roof.
The silence feels heavy.

✅ Example Output
{
  "emotion": "tension",
  "narrative_purpose": "to create suspense and foreshadow a pivotal moment",
  "visual_mood": "dark, foreboding, isolated atmosphere",
  "camera_style": "static framing focused on subtle facial reactions",
  "confidence": 0.9
}

🧭 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/SakethSumanBathini/scene-intent-engine.git
cd scene-intent-engine

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup environment variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here


⚠️ .env is ignored by git for security.

5️⃣ Run the app
streamlit run app.py

🎯 Hackathon Takeaway

This project demonstrates how LLM-based reasoning can:

Convert unstructured creative text

Into actionable cinematic intent

Saving time during early film production

While augmenting (not replacing) human creativity

🗺️ Future Roadmap (Post-Hackathon)

📂 Multi-scene screenplay upload & batch analysis

🎞️ Automatic shot-list generation per scene

🧩 Integration with storyboard / previz tools
(Unreal Engine, Blender, Runway)

🎬 Director Mode vs Writer Mode outputs

📊 Scene-level confidence dashboard
