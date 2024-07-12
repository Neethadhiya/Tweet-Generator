#pip install streamlit
import os
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key

st.title("Tweet Generator - V 🐦")

st.subheader("🚀 Generate tweets on any topic")

topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)


# Import ChatOpenAI module
from langchain_openai import ChatOpenAI

# Initialize OpenAI's GPT 3.5 model
gpt3_model = ChatOpenAI(model_name = "gpt-3.5-turbo-0125")


if st.button("Generate"):
    prompt = f"Give me {number} tweets on {topic}."
    response = gpt3_model.invoke(prompt)
    st.write(response.content)


# python test.py
