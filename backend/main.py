from fastapi import FastAPI
from database import SessionLocal
from datetime import date

from models.mother import Mother
from models.pregnancy import Pregnancy
from models.child import Child
from models.health_event import HealthEvent
from schemas.journey import JourneyResponse
from journey.engine import build_journey, get_next_milestone
from journey.gap_detector import detect_gaps

from schemas.mother import MotherCreate, MotherResponse
from schemas.pregnancy import PregnancyCreate, PregnancyResponse
from schemas.child import ChildCreate, ChildResponse
from schemas.health_event import HealthEventCreate, HealthEventResponse


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Saathi API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/mothers", response_model=MotherResponse)
def create_mother(mother: MotherCreate):
    db = SessionLocal()

    new_mother = Mother(
        name=mother.name,
        date_of_birth=mother.date_of_birth,
        phone=mother.phone,
        address=mother.address
    )

    db.add(new_mother)
    db.commit()
    db.refresh(new_mother)

    db.close()

    return new_mother


@app.get("/mothers/{mother_id}", response_model=MotherResponse)
def get_mother(mother_id: int):
    db = SessionLocal()

    mother = db.query(Mother).filter(Mother.id == mother_id).first()

    db.close()

    if mother is None:
        return {"error": "Mother not found"}

    return mother


@app.post("/pregnancies", response_model=PregnancyResponse)
def create_pregnancy(pregnancy: PregnancyCreate):
    db = SessionLocal()

    new_pregnancy = Pregnancy(
        mother_id=pregnancy.mother_id,
        last_menstrual_period=pregnancy.last_menstrual_period,
        expected_delivery_date=pregnancy.expected_delivery_date
    )

    db.add(new_pregnancy)
    db.commit()
    db.refresh(new_pregnancy)

    db.close()

    return new_pregnancy


@app.get("/mothers/{mother_id}/pregnancy", response_model=PregnancyResponse)
def get_mother_pregnancy(mother_id: int):
    db = SessionLocal()

    pregnancy = (
        db.query(Pregnancy)
        .filter(Pregnancy.mother_id == mother_id)
        .first()
    )

    db.close()

    if pregnancy is None:
        return {"error": "Pregnancy not found"}

    return pregnancy


@app.post("/children", response_model=ChildResponse)
def create_child(child: ChildCreate):
    db = SessionLocal()

    new_child = Child(
        pregnancy_id=child.pregnancy_id,
        name=child.name,
        date_of_birth=child.date_of_birth,
        gender=child.gender
    )

    db.add(new_child)
    db.commit()
    db.refresh(new_child)

    db.close()

    return new_child


@app.get("/mothers/{mother_id}/child", response_model=ChildResponse)
def get_mother_child(mother_id: int):
    db = SessionLocal()

    pregnancy = (
        db.query(Pregnancy)
        .filter(Pregnancy.mother_id == mother_id)
        .first()
    )

    if pregnancy is None:
        db.close()
        return {"error": "Pregnancy not found"}

    child = (
        db.query(Child)
        .filter(Child.pregnancy_id == pregnancy.id)
        .first()
    )

    db.close()

    if child is None:
        return {"error": "Child not found"}

    return child


@app.post("/health-events", response_model=HealthEventResponse)
def create_health_event(event: HealthEventCreate):
    db = SessionLocal()

    new_event = HealthEvent(
        pregnancy_id=event.pregnancy_id,
        event_type=event.event_type,
        event_date=event.event_date,
        status=event.status,
        notes=event.notes
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    db.close()

    return new_event


@app.get(
    "/pregnancies/{pregnancy_id}/health-events",
    response_model=list[HealthEventResponse]
)
def get_health_events(pregnancy_id: int):
    db = SessionLocal()

    events = (
        db.query(HealthEvent)
        .filter(HealthEvent.pregnancy_id == pregnancy_id)
        .order_by(HealthEvent.event_date)
        .all()
    )

    db.close()

    return events


@app.get("/health-events/{event_id}", response_model=HealthEventResponse)
def get_health_event(event_id: int):
    db = SessionLocal()

    event = (
        db.query(HealthEvent)
        .filter(HealthEvent.id == event_id)
        .first()
    )

    db.close()

    if event is None:
        return {"error": "Health event not found"}

    return event


@app.get("/mothers/{mother_id}/journey", response_model=JourneyResponse)
def get_mother_journey(mother_id: int):
    db = SessionLocal()

    pregnancy = (
        db.query(Pregnancy)
        .filter(Pregnancy.mother_id == mother_id)
        .first()
    )

    if pregnancy is None:
        db.close()
        return {"error": "Pregnancy not found"}

    events = (
        db.query(HealthEvent)
        .filter(HealthEvent.pregnancy_id == pregnancy.id)
        .order_by(HealthEvent.event_date)
        .all()
    )

    db.close()

    journey = build_journey(events, pregnancy)

    next_milestone = get_next_milestone(journey)

    gaps = detect_gaps(journey, pregnancy, date.today())

    return {
        "mother_id": mother_id,
        "pregnancy_id": pregnancy.id,
        "next_milestone": next_milestone,
        "gaps": gaps,
        "completed": journey["completed"],
        "current": journey["current"],
        "upcoming": journey["upcoming"],
        "verification_needed": journey["verification_needed"],
        "events": events
    }
