# models.py
from sqlalchemy import Column, Integer, String
from database.initiate import Base  # Assuming Base is defined in database.py
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)   
    email = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)

    notes = relationship("Note", back_populates="user")  # <-- This defines user.notes