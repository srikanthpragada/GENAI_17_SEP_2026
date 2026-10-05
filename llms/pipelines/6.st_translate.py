# pip install -q streamlit
import streamlit as st
from transformers import pipeline

translator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-3B-Instruct"
)

st.title("English to Hindi")
text  = st.text_input("Enligsh Text", "" )
if len(text) > 0:
    prompt = f"Translate English to Hindi\n{text}. Do not give any more details"
    hindi = translator(prompt, return_full_text=False)
    st.write("<h2>" + hindi[0]["generated_text"] + "</h2>",
             unsafe_allow_html=True)



     