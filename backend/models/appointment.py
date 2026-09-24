from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    mother_id = Column(Integer, ForeignKey("mothers.id"), nullable=False)

    appointment_type = Column(String, nullable=False)
    appointment_date = Column(Date, nullable=False)
    status = Column(String, nullable=True)
    notes = Column(String, nullable=True)