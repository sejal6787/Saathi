from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from database import Base


class HealthEvent(Base):
    __tablename__ = "health_events"

    id = Column(Integer, primary_key=True, index=True)
    pregnancy_id = Column(Integer, ForeignKey("pregnancies.id"), nullable=True)

    event_type = Column(String, nullable=False)
    event_date = Column(Date, nullable=False)
    status = Column(String, nullable=True)
    notes = Column(Text, nullable=True)