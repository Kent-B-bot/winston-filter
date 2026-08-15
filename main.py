from fastapi import FastAPI
from models.winston_response import WinstonResponse
from scoring.winston_engine import compute_winston_score

app = FastAPI(title="Winston Filter API")

@app.get("/winston/{symbol}", response_model=WinstonResponse)
def get_winston(symbol: str):
    """
    Main Winston Filter endpoint.
    Computes the Winston Score and returns the full JSON response.
    """
    return compute_winston_score(symbol)
