import streamlit as st

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_community.llms import Ollama

# Streamlit UI

st.set_page_config(page_title="LangChain Chatbot", page_icon="🤖")
st.title("🤖 LangChain Chatbot")

input_txt = st.text_input("Please enter your query")

# Prompt

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Your name is MUTHUSELVAM'S Assistant."),
    ("human", "{query}")
])

# LLM (Ollama)

llm = Ollama(model="llama2")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# Run

if input_txt:
    response = chain.invoke({"query": input_txt})
    st.write(response)
