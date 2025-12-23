"""FastAPI application entrypoint."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import AnalyzeRequest, AnalyzeResponse

app = FastAPI(title="Gmail Agent Backend", version="0.1.0")

# Enable CORS for the dev frontend and the Chrome extension.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_origin_regex=r"^chrome-extension://.*$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    """Simple health check endpoint."""

    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(payload: AnalyzeRequest) -> AnalyzeResponse:
    """Analyze an email payload.

    This is intentionally a placeholder response to be replaced later.
    """

    return AnalyzeResponse(
        summary="Analysis placeholder: replace with real logic.",
        metadata_echo=payload.metadata,
    )
