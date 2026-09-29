from pydantic import BaseModel, Field


class RoyaltyRecord(BaseModel):
    artist: str = Field(..., min_length=1)
    song: str = Field(..., min_length=1)
    platform: str = Field(..., min_length=1)
    reporting_period: str = Field(..., min_length=1)
    streams: int = Field(..., ge=0)
    expected_rate: float = Field(..., ge=0)
    actual_royalty: float = Field(..., ge=0)
    currency: str = Field(default="USD", min_length=1)