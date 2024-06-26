from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, validates
import re


# DeclarativeBase is called an Abstract Base Class - our SQL Alchemy models will inherit from this class
class Base(DeclarativeBase):
    pass


class EmailAddress(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'EmailAddress(email={self.email}'

    @validates('email')
    def validate_email(self, key, address):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(pattern, address):
            raise ValueError('Invalid email address')
        if key != 'email':
            raise ValueError('Key must be "email"')
        return address
