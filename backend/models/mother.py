from sqlalchemy import Column, Integer, String, Date
from database import Base


class Mother(Base):
    __tablename__ = "mothers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=True)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)