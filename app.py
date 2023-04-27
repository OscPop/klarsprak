import openai
import os
import streamlit as st
import pandas as pd
import numpy as np


openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Klarspråksmaskineriet")