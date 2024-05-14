from pydantic import BaseModel


class SolveRequest(BaseModel):
    prompt: str
