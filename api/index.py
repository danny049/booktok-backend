from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ScanRequest(BaseModel):
    imageBase64: str


class Candidate(BaseModel):
    title: str
    author: str | None = None
    confidence: float | None = None


class ScanResponse(BaseModel):
    candidates: list[Candidate]


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/scan", response_model=ScanResponse)
async def scan(req: ScanRequest) -> ScanResponse:
    candidates = [
        Candidate(
            title="The Great Gatsby", author="F. Scott Fitzgerald", confidence=0.95
        ),
        Candidate(
            title="The Catcher in the Rye", author="J.D. Salinger", confidence=0.90
        ),
        Candidate(title="1984", author="George Orwell", confidence=0.85),
    ]
    return ScanResponse(candidates=candidates)
