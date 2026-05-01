from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateRequest(BaseModel):
    url: str
    expires_at: Optional[datetime] = None


class CreateResponse(BaseModel):
    token: str
    short_url: str
    qr_code_url: str
    original_url: str


class QRInfoResponse(BaseModel):
    token: str
    original_url: str
    created_at: datetime
    updated_at: datetime
    expires_at: Optional[datetime]
    is_deleted: bool


class UpdateRequest(BaseModel):
    url: Optional[str] = None
    expires_at: Optional[datetime] = None
