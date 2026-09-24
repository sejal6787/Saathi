from pydantic import BaseModel

from schemas.health_event import HealthEventResponse


class JourneyResponse(BaseModel):

    mother_id: int
    pregnancy_id: int
    next_milestone: dict | None

    completed: list[dict]
    current: list[dict]
    upcoming: list[dict]
    verification_needed: list[dict]
    gaps: list[dict]
    events: list[HealthEventResponse]