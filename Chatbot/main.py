from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()


os.environ["GOOGLE_KEY"]=os.getenv("GOOGLE_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

GOOGLE_KEY = os.getenv("GOOGLE_KEY")

promt=ChatPromptTemplate.from_messages(
    [
    ("system","you are a helpful for assistance"),
    ("user","question :{question}")
]
)

st.title("Basic chatbot model")
user_input=st.text_input("Enter your topic")
llm_model=ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            google_api_key=GOOGLE_KEY,
            convert_system_message_to_human=True)
output=StrOutputParser()
chain_model=promt|llm_model|output

if user_input:
    st.button('submit')
    st.write(chain_model.invoke({'question':user_input}))
