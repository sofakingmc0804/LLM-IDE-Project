from pydantic import BaseModel
from typing import List

class BiasResult(BaseModel):
    bias_score: float
    categories: List[str]

class ValidateRequest(BaseModel):
    text: str

class ValidateResponse(BaseModel):
    verdict: str
    details: dict
