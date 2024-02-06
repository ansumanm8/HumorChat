from pydantic import BaseModel

class CHAT(BaseModel):
    question: str
