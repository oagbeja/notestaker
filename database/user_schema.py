# models.py
from sqlalchemy import Column, Integer, String
from database.initiate import Base  # Assuming Base is defined in database.py

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)   
    email = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)

