import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_content(prompt):
    response = model.generate_content(
<<<<<<< HEAD
    prompt,
    generation_config={
        "temperature": 0.8,
        "max_output_tokens": 2048,
    }
)
=======
        prompt,
        generation_config={
            "temperature": 0.7,
            "max_output_tokens": 1000,
        }
    )
>>>>>>> 41cbbf640db0a1284aab3668fe8bba63e5f21a2c

    return response.text