from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Person

# Connect to the activities database
engine = create_engine('sqlite:///activities.sqlite', echo=True)

# Start a session - we'll leave it open in this file, so will need to close it later
sess = Session(engine)

# Read from the person table
andrew = sess.query(Person).filter_by(last_name='Dales').one_or_none()
people = sess.query(Person).all()
