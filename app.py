import openai
import os
import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def prompt_template(prompt):

    messages = []

    system_prompt = f"""
    Du är en hjälpsam AI-assistent som ska hjälpa användaren att skriva om text till klarspråk.
    Språknivån ska vara relevant till kontexten klarspråk för myndighetssvenska. 
    Du får under inga omständigheter ändra informationen eller lägga till information.
    Svara endast med den omskrivna texten.
    """

    messages.append({"role": "system", "content": system_prompt})

    user_prompt = f"""
    Här kommer meddelandet som ska skrivas om till klarspråk:
    '{prompt}'
    """

    messages.append({"role": "user", "content": user_prompt})

    return messages


st.title("Klarspråksmaskineriet")
st.write("Det här är en prototyp för att skriva om text till klarspråk. Det är en del av projektet Klarspråksmaskineriet. \
         All information går i nuläget via amerikanska molntjänster, så klistra INTE in känslig information i fältet nedan.")


# Välja modell
model = st.selectbox("Här kan du välja vilken AI-modell som ska användas:", ["gpt-3.5-turbo", "gpt-4-0314"], index=0)



# Skriva in prompt
prompt = st.text_area("Klistra in text som ska skrivas om till klarspråk: ", 
                      placeholder="", 
                      height=600)

if len(prompt) > 0:
  completion = openai.ChatCompletion.create(
    model=model,
    messages=prompt_template(prompt)
  )

  st.write(completion.choices[0].message["content"])






