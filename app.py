import openai
import os
import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def prompt_template(prompt):

    full_prompt = f"""
    Du är en hjälpsam AI-assistent som ska hjälpa användaren att skriva om text till klarspråk.
    Språknivån ska vara relevant till kontexten klarspråk för myndighetssvenska. 
    Du får under inga omständigheter ändra informationen eller lägga till information.
    Svara endast med den omskrivna texten.
    
    Här kommer meddelandet som ska skrivas om till klarspråk:
    '{prompt}'
    """

    return full_prompt


st.title("Klarspråksmaskineriet")

# Välja modell
model = st.selectbox("Välj modell", ["gpt-3.5-turbo", "gpt-4-0314"], index=0)

st.write("Det här är en prototyp för att skriva om text till klarspråk. Det är en del av projektet Klarspråksmaskineriet.")


# Skriva in prompt
prompt = st.text_area("Klistra in text som ska skrivas om till klarspråk: ", placeholder="den her teksten er int klearsprok")

completion = openai.ChatCompletion.create(
  model=model,
  messages=[
    {"role": "user", "content": prompt_template(prompt)}
  ]
)

st.write(completion.choices[0].message["content"])






