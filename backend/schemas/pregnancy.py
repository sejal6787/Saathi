from datetime import date
from pydantic import BaseModel, ConfigDict


class PregnancyCreate(BaseModel):
    mother_id: int
    last_menstrual_period: date | None = None
    expected_delivery_date: date | None = None


class PregnancyResponse(BaseModel):
    id: int
    mother_id: int
    last_menstrual_period: date | None = None
    expected_delivery_date: date | None = None

    model_config = ConfigDict(from_attributes=True)