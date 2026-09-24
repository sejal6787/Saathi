from datetime import date
from pydantic import BaseModel, ConfigDict


class HealthEventCreate(BaseModel):
    pregnancy_id: int | None = None
    event_type: str
    event_date: date
    status: str | None = None
    notes: str | None = None


class HealthEventResponse(BaseModel):
    id: int
    pregnancy_id: int | None = None
    event_type: str
    event_date: date
    status: str | None = None
    notes: str | None = None

    model_config = ConfigDict(from_attributes=True)