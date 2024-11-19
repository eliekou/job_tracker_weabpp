from pydantic import BaseModel
from typing import Optional
from datetime import date


class JobApplication(BaseModel):
    job_title: str
    company: str
    date_applied: Optional[date] = None  # Optional; defaults to None if not provided
    status: Optional[str] = "Pending"  # Defaults to "Pending"
