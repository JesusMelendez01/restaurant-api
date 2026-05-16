from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime

from app.database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    address = Column(String, nullable=False)

    city = Column(String, nullable=False)

    cuisine_type = Column(String, nullable=False)

    rating = Column(Float, nullable=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    