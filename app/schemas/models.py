from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    brand: str
    competitors: list[str]
    prompts: list[str]