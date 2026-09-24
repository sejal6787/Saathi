from datetime import date
from pydantic import BaseModel, ConfigDict


class MotherCreate(BaseModel):
    name: str
    date_of_birth: date | None = None
    phone: str | None = None
    address: str | None = None


class MotherResponse(BaseModel):
    id: int
    name: str
    date_of_birth: date | None = None
    phone: str | None = None
    address: str | None = None

    model_config = ConfigDict(from_attributes=True)