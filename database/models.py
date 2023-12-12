from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

# Add more classes for additional tables as needed

# Example: class Loan(Base):
#     __tablename__ = 'loans'
#     id = Column(Integer, primary_key=True)
#     amount = Column(Integer)
#     borrower_id = Column(Integer, ForeignKey('users.id'))
#     borrower = relationship(User)
