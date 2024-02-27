from typing import List, Any
from pydantic import BaseModel


class Prompt(BaseModel):
    user_prompt: str
    system_prompt: str


class Response(BaseModel):
    text: str