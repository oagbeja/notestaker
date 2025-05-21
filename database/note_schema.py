# models.py
from sqlalchemy import Column, Integer, String,Enum as SqlEnum, ForeignKey, DateTime, func
from database.initiate import Base  # Assuming Base is defined in database.py
from sqlalchemy.orm import relationship
from models.note_model import Categories

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)   
    title = Column(String(50), index=True, nullable=True)
    details = Column(String(255), nullable=True)

    # Category from Enum
    category = Column(SqlEnum(Categories), nullable=False, default=Categories.default)

    # Foreign key to user ID
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="notes")

    # Timestamp
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

