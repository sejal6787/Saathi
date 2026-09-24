from datetime import date
from pydantic import BaseModel, ConfigDict


class AppointmentCreate(BaseModel):
    mother_id: int
    appointment_type: str
    appointment_date: date
    status: str | None = None
    notes: str | None = None


class AppointmentResponse(BaseModel):
    id: int
    mother_id: int
    appointment_type: str
    appointment_date: date
    status: str | None = None
    notes: str | None = None

    model_config = ConfigDict(from_attributes=True)