from database import Base, engine
from models.mother import Mother
from models.pregnancy import Pregnancy
from models.child import Child
from models.health_event import HealthEvent
from models.user import User
from models.appointment import Appointment


Base.metadata.create_all(bind=engine)

print("Tables created successfully!")