import os
from dotenv import load_dotenv
import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "qna-chatbot"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant, please respond to user queries"),
        ("user", "question:{user_input}")
    ]
)

def generate_response(llm_model, temperature, max_tokens, user_input):
    llm = OllamaLLM(model= llm_model)
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"user_input" : user_input})
    st.write(response)

st.title("QnA Chatbot")

st.sidebar.title("Settings")

llm = st.sidebar.selectbox("Select an AI model", ["gemma:2b", "llama:3b", "qwen:2b"])
temperature = st.sidebar.slider("Temperature", min_value= 0.0, max_value= 1.0, value= 0.7)
max_tokens = st.sidebar.slider("max_tokens", min_value= 50, max_value= 300, value= 150)

st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(llm, temperature, max_tokens, user_input)
    st.write(response)
else:
    st.write("Ask your question!!")