from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import EmailAddress

# Connect to the activities database
engine = create_engine('sqlite:///emails.sqlite', echo=True)
sess = Session(engine)
