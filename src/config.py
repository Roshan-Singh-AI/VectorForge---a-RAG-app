import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

groq_api_key = os.getenv("groq_api_key")
if groq_api_key is not None:
    os.environ["GROQ_API_KEY"] = groq_api_key
else:
    raise ValueError("groq_api_key environment variable is not set.")

groq_llm_model = ChatGroq(model=os.getenv("groq_llama_model", "llama-3.3-70b-versatile"), streaming=True)