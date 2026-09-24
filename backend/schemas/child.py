from datetime import date
from pydantic import BaseModel, ConfigDict


class ChildCreate(BaseModel):
    pregnancy_id: int
    name: str | None = None
    date_of_birth: date | None = None
    gender: str | None = None


class ChildResponse(BaseModel):
    id: int
    pregnancy_id: int
    name: str | None = None
    date_of_birth: date | None = None
    gender: str | None = None

    model_config = ConfigDict(from_attributes=True)