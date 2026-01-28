# from groq import Groq
# import os
# from dotenv import load_dotenv

# load_dotenv()

# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# response = client.chat.completions.create(
#     model="llama-3.1-8b-instant",
#     messages=[
#         {"role": "user", "content": "Say hello in one sentence."}
#     ]
# )

# print(response.choices[0].message.content)






# from groq import Groq
# from dotenv import load_dotenv
# import os

# load_dotenv()

# MODEL_NAME = "llama-3.1-70b-versatile" # 👈 THIS decides the model
# print("USING MODEL:", MODEL_NAME)



# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")
# )

# response = client.chat.completions.create(
#     model="llama-3.1-70b-versatile",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a cinematic scene intent extraction engine. Output strict JSON only."
#         },
#         {
#             "role": "user",
#             "content": scene_text
#         }
#     ],
#     temperature=0.2,
#     max_tokens=700
# )

# output = response.choices[0].message.content


# def analyze_scene(scene_text):
#     response = client.chat.completions.create(
#         model=MODEL_NAME,
#         messages=[...]
#     )
#     return response

# # test_groq.py
# # Quick sanity test for Groq API + model availability



# # Load environment variables
# load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# if not GROQ_API_KEY:
#     raise RuntimeError("GROQ_API_KEY not found in .env")

# client = Groq(api_key=GROQ_API_KEY)

# # Change this to test any model
# MODEL_NAME = "llama-3.1-70b-instruct"
# # MODEL_NAME = "llama-3.1-8b-instant"

# print("Testing model:", MODEL_NAME)

# try:
#     response = client.chat.completions.create(
#         model=MODEL_NAME,
#         messages=[
#             {"role": "system", "content": "You are a test assistant."},
#             {"role": "user", "content": "Reply with the word OK only."}
#         ],
#         temperature=0,
#         max_tokens=5,
#     )

#     print("✅ Model works!")
#     print("Response:", response.choices[0].message.content)

# except Exception as e:
#     print("❌ Model test failed")
#     print(e)


# test_groq.py
# Standalone sanity test for Groq API + model availability
# This file is ONLY for testing – not used by app.py

import os
from dotenv import load_dotenv
from groq import Groq

# ----------------------------------------
# Load environment variables
# ----------------------------------------
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError("[Error] GROQ_API_KEY not found in .env file")

# ----------------------------------------
# Initialize Groq client
# ----------------------------------------
client = Groq(api_key=GROQ_API_KEY)

# ----------------------------------------
# Choose model to test
# ----------------------------------------
MODEL_NAME = "llama-3.3-70b-versatile"
# MODEL_NAME = "llama-3.1-8b-instant"   # fallback test

print("[Search] Testing Groq model:", MODEL_NAME)

# ----------------------------------------
# Simple test prompt
# ----------------------------------------
try:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "Reply ONLY with the word OK."},
            {"role": "user", "content": "Test"}
        ],
        temperature=0,
        max_tokens=5,
    )

    print("[Check] Model works successfully!")
    print("[Brain] Model response:", response.choices[0].message.content)

except Exception as e:
    print("[Error] Model test failed")
    print(e)
