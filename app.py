import openai
import os
import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Klarspråksmaskineriet")

txt = st.text_area("Klistra in text som ska skrivas om till klarspråk: ",
             placeholder="den her teksten er int klearsprok")


completion = openai.ChatCompletion.create(
  model="gpt-4-0314",
  messages=[
    {"role": "user", "content": txt}
  ]
)


st.write(completion.choices[0].message)