import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8080/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8080/graduate_essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

    ## streamlit framework

st.title('Langchain Demo With LLAMA2 API and ChatOpenAI')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a Graduate level essay on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))