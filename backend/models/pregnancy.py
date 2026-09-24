from sqlalchemy import Column, Integer, Date, ForeignKey
from database import Base


class Pregnancy(Base):
    __tablename__ = "pregnancies"

    id = Column(Integer, primary_key=True, index=True)
    mother_id = Column(Integer, ForeignKey("mothers.id"), nullable=False)
    last_menstrual_period = Column(Date, nullable=True)
    expected_delivery_date = Column(Date, nullable=True)