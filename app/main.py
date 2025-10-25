# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.model import analiza


app = FastAPI(title="Sentiment API", version="1.0.0")

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzeBatchRequest(BaseModel):
    texts: List[str]

@app.get("/health")
def health():
    return {"status": "ok"}

# GET: prueba rápida desde navegador/PowerShell
@app.get("/analyze")
def analyze_get(text: str):
    try:
        return {"text": text, **analiza(text)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# POST: consumo “real” (JSON body)
@app.post("/analyze")
def analyze_post(req: AnalyzeRequest):
    try:
        return {"text": req.text, **analiza(req.text)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze_batch")
def analyze_batch(req: AnalyzeBatchRequest):
    try:
        results = [{"text": t, **analiza(t)} for t in req.texts]
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
