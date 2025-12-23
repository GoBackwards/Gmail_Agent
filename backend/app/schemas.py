"""Pydantic request/response models for the API."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    """Incoming payload for the /analyze endpoint."""

    email_text: str = Field(..., description="Raw email text to analyze.")
    metadata: Optional[Dict[str, Any]] = Field(
        default=None, description="Optional metadata attached to the email."
    )


class AnalyzeResponse(BaseModel):
    """Placeholder response for the /analyze endpoint."""

    summary: str = Field(..., description="Placeholder analysis summary.")
    metadata_echo: Optional[Dict[str, Any]] = Field(
        default=None, description="Echoes input metadata for now."
    )
