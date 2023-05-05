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
st.write("Det här är en prototyp för att skriva om text till klarspråk med hjälp av chatboten GPT från OpenAI. All information går i nuläget via amerikanska molntjänster, så klistra INTE in känslig information i fältet nedan. \
         Detta är en tidig testversion av en sorts klarspråksassistent som är under utveckling, det är alltså inte garanterat att appen fungerar konstant. Den kan endast lämna förbättringsförslag på ren text och inte på layout eller bilder.\
         Det primära användningsområdet bedöms vara de som vill få inspiration på hur man kan skriva om text till klarspråk. Läs alltid igenom texten som genereras med kritiska ögon och använd sunt förnuft. Det kan hända att AI\:n använder en omformulering som ändrar innebörden av texten.")

st.write("Med det sagt, välkommen att testa! Lämna gärna feedback/tankar på om det är användbart och hur man skulle kunna utveckla det vidare. Skriv gärna till mig (Oscar) på teams/mail om ni har frågor eller funderingar.")

with st.expander("Hur funkar det?"):
    st.write("Appen använder sig av en AI-modell som heter GPT från OpenAI. Det är en sorts chatbot som kan skriva text baserat på en prompt (en kort beskrivning av vad som ska skrivas). \
            AI\:n har tränats på en stor mängd text från internet och kan därför skriva text som liknar mänsklig text. Det finns många olika AI-modeller att välja på från OpenAI, här kan 2 olika användas: GPT-3.5-turbo och GPT-4. GPT-3.5-turbo är lite snabbare men GPT-4 ska vara lite bättre. \
            Det går att läsa mer om GPT-4 här: https://openai.com/product/gpt-4. Mer teknisk information angående modeller går att erhålla här: https://platform.openai.com/docs/models/overview.")
            
    st.write("För att underlätta för användaren har jag redan lagt in en prompt som berättar lite för AI\:n vad den ska göra. Det fullständiga meddelandet till AI\:n blir alltså \
            mina instruktioner, följt utav meddelandet som ska skrivas om till klarspråk. ")
   
    st.markdown("## Mina instruktioner till AI\:n är:")
    st.markdown("*Du är en hjälpsam AI-assistent som ska hjälpa användaren att skriva om text till klarspråk.\
    Språknivån ska vara relevant till kontexten klarspråk för myndighetssvenska. \
    Du får under inga omständigheter ändra informationen eller lägga till information.\
    Svara endast med den omskrivna texten.*")
    st.markdown("*Här kommer meddelandet som ska skrivas om till klarspråk:*")
    st.markdown("[meddelandet som ska skrivas om]")

# Välja modell
model = st.selectbox("Här kan du välja vilken AI-modell som ska användas:", ["gpt-3.5-turbo", "gpt-4-0314"],
                    index=0,
                    on_change=proc)



# Skriva in prompt
st.text_area("Klistra in text som ska skrivas om till klarspråk (och tryck CTRL + ENTER): ", 
            placeholder="den her teksten er int klearsprok", 
            height=600,
            on_change=proc,
            key="prompt")



st.write(st.session_state.completion_message)




