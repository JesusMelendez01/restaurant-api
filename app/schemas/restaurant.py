from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class RestaurantCreate(BaseModel):
    name: str = Field(..., min_length=1)
    address: str
    city: str
    cuisine_type: str
    rating: float = Field(..., ge=0.0, le=5.0)
    is_active: bool = True


class RestaurantUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    cuisine_type: Optional[str] = None
    rating: Optional[float] = Field(None, ge=0.0, le=5.0)
    is_active: Optional[bool] = None


class RestaurantResponse(BaseModel):
    id: int
    name: str
    address: str
    city: str
    cuisine_type: str
    rating: float
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)