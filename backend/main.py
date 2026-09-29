from fastapi import FastAPI

from models.royalty import RoyaltyRecord
from services.royalty_detector import calculate_royalty_leakage


app = FastAPI(
    title="Independent Musician Royalty Leakage Detective",
    description="API for detecting potential royalty leakage for independent musicians.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Independent Musician Royalty Leakage Detective API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/analyze-royalty")
def analyze_royalty(record: RoyaltyRecord):
    analysis = calculate_royalty_leakage(
        streams=record.streams,
        expected_rate=record.expected_rate,
        actual_royalty=record.actual_royalty,
    )

    return {
        "artist": record.artist,
        "song": record.song,
        "platform": record.platform,
        "reporting_period": record.reporting_period,
        "streams": record.streams,
        "currency": record.currency,
        **analysis,
    }