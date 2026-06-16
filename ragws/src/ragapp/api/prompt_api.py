#create prompt input using post operation

from fastapi import FastAPI
from ragapp.api.prompt_request import PromptRequest
from ragapp.utils.rag_engine import receive_prompt

fastapi=FastAPI(
    title="RAG pipeline API",
    description="API for RAG pipeline",
    version="1.0.0"
    
)
@fastapi.post("/prompt")
def create_prompt_input(prompt_request: PromptRequest):
    
     return receive_prompt(prompt_request.prompt)
    