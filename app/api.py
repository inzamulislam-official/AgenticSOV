from fastapi import FastAPI
from app.schemas.models import AnalysisRequest


app = FastAPI(
    title="AgenticSOV",
    description="AI/LLM Share-of-Voice Measurement Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "product": "AgenticSOV",
        "purpose": "Measure brand visibility and recommendation share in LLM-generated answers."
    }


@app.post("/analyze")
def analyze(request: AnalysisRequest):
    return {
        "brand": request.brand,
        "competitors": request.competitors,
        "prompt_count": len(request.prompts)
    }