from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import ollama
from langchain_core.output_parsers import StrOutputParser
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

promt=ChatPromptTemplate.from_messages(
    [
        ("system",'Hi how can i assist you?'),
        ('user','question:{question}')
    ]
)

llm_model=ollama(model='Gemma 3')
output=StrOutputParser()
chain_model=promt | llm_model | output

st.title("Basic LLM APP")
user_input=st.text_input("Enter yout topic")

# userinput
if user_input:
    st.button("Submit")
    
    st.write(chain_model.invoke({'question':user_input}))