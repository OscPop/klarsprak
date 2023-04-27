import openai
import os
import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Klarspråksmaskineriet")

prompt = st.text_area("Klistra in text som ska skrivas om till klarspråk: ",
             placeholder="den her teksten er int klearsprok")


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


completion = openai.ChatCompletion.create(
  model="gpt-4-0314",
  messages=[
    {"role": "user", "content": prompt_template(prompt)}
  ]
)


st.write(completion.choices[0].message)