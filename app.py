import openai
import os
import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv


load_dotenv()
openai.api_key = st.secrets["OPENAI_API_KEY"] #os.getenv("OPENAI_API_KEY")


# Initiera session state
if "completion_message" not in st.session_state:
   st.session_state.completion_message = ""
if "prompt" not in st.session_state:
    st.session_state.prompt = ""


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



def proc():
    if st.session_state.prompt != "":
      completion = openai.ChatCompletion.create(
        model=model,
        messages=prompt_template(st.session_state.prompt)
      )
      completion_message = completion.choices[0].message["content"]
      st.session_state.completion_message = completion_message




st.title("Klarspråksmaskineriet")
st.write("Det här är en prototyp för att skriva om text till klarspråk med hjälp av chatboten GPT från OpenAI. All information går i nuläget via amerikanska molntjänster, så klistra INTE in känslig information i fältet nedan.")
st.write("Det finns många olika AI-modeller att välja på från OpenAI, här kan 2 olika användas: GPT-3.5-turbo och GPT-4.")
st.write("GPT-3.5-turbo är lite snabbare men GPT-4 ska vara lite bättre.")
st.write("Det går att läsa mer om modellerna här: https://openai.com/blog/gpt-3-5b/ och här: https://openai.com/blog/gpt-4/")

st.write("Detta är en tidig testversion av en sorts klarspråksassistent som är under utveckling.")
st.write("Den kan endast lämna förbättringsförslag på ren text och inte på layout eller bilder.")
st.write("Det primära användningsområdet bedöms vara de som vill få inspiration på hur man kan skriva om text till klarspråk.")
st.write("Läs alltid igenom texten som genereras med kritiska ögon och använd sunt förnuft. Det kan hända att AI:n använder en omformulering som ändrar innebörden av texten.")


# Välja modell
model = st.selectbox("Här kan du välja vilken AI-modell som ska användas:", ["gpt-3.5-turbo", "gpt-4-0314"],
                    index=0,
                    on_change=proc)



# Skriva in prompt
st.text_area("Klistra in text som ska skrivas om till klarspråk: ", 
            placeholder="den her teksten er int klearsprok", 
            height=600,
            on_change=proc,
            key="prompt")



st.write(st.session_state.completion_message)




