from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base


class Child(Base):
    __tablename__ = "children"

    id = Column(Integer, primary_key=True, index=True)
    pregnancy_id = Column(Integer, ForeignKey("pregnancies.id"), nullable=False)
    name = Column(String, nullable=True)
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String, nullable=True)