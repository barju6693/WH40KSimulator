import os

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    llm_model: str = os.getenv("LLM_MODEL","")
    llm_api_key: str = os.getenv("LLM_API_KEY","")
    llm_url: str = os.getenv("LLM_URL","")

    langfuse_public_key: str = os.getenv("LANGFUSE_PUBLIC_KEY","")
    langfuse_secret_key: str = os.getenv("LANGFUSE_SECRET_KEY","")
    langfuse_host: str = os.getenv("LANGFUSE_HOST","")


settings = Settings()