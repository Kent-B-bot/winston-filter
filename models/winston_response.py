from pydantic import BaseModel
from typing import Optional, Dict, Any

class WinstonPillar(BaseModel):
    score: Optional[int]
    percentile: Optional[float]
    metrics: Dict[str, Any]
    facts: list[str]

class WinstonResponse(BaseModel):
    symbol: str
    name: str
    sector: str
    as_of_date: str

    scorable: bool
    winston_score: Optional[int]
    winston_band: Optional[str]

    pillars: Dict[str, WinstonPillar]
