from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('openai_key1')

app = FastAPI(
    title='Langchain Server',
    version= "1.0",
    description="API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

#Create objects for multiple models
model=ChatOpenAI()
llm=Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an essay about {topic} for a graduate level student with 250 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/graduate_essay"
)

if __name__ == '__main__':
    uvicorn.run(app,host="localhost",port=8080)



