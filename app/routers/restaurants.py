from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.restaurant import Restaurant

from app.schemas.restaurant import (
    RestaurantCreate,
    RestaurantUpdate,
    RestaurantResponse
)

router = APIRouter(
    prefix="/api/restaurants",
    tags=["Restaurants"]
)


@router.post("/", response_model=RestaurantResponse, status_code=201)
def create_restaurant(
    restaurant: RestaurantCreate,
    db: Session = Depends(get_db)
):

    db_restaurant = Restaurant(**restaurant.model_dump())

    db.add(db_restaurant)

    db.commit()

    db.refresh(db_restaurant)

    return db_restaurant


@router.get("/")
def get_restaurants(
    city: str | None = None,
    is_active: bool | None = None,
    db: Session = Depends(get_db)
):

    query = db.query(Restaurant)

    if city:
        query = query.filter(Restaurant.city == city)

    if is_active is not None:
        query = query.filter(Restaurant.is_active == is_active)

    restaurants = query.all()

    return {
        "restaurants": restaurants
    }


@router.get("/{restaurant_id}", response_model=RestaurantResponse)
def get_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db)
):

    restaurant = db.query(Restaurant).filter(
        Restaurant.id == restaurant_id
    ).first()

    if not restaurant:

        raise HTTPException(
            status_code=404,
            detail="Restaurante no encontrado"
        )

    return restaurant


@router.put("/{restaurant_id}", response_model=RestaurantResponse)
def update_restaurant(
    restaurant_id: int,
    restaurant_data: RestaurantUpdate,
    db: Session = Depends(get_db)
):

    restaurant = db.query(Restaurant).filter(
        Restaurant.id == restaurant_id
    ).first()

    if not restaurant:

        raise HTTPException(
            status_code=404,
            detail="Restaurante no encontrado"
        )

    update_data = restaurant_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():

        setattr(restaurant, key, value)

    db.commit()

    db.refresh(restaurant)

    return restaurant


@router.delete("/{restaurant_id}", status_code=204)
def delete_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db)
):

    restaurant = db.query(Restaurant).filter(
        Restaurant.id == restaurant_id
    ).first()

    if not restaurant:

        raise HTTPException(
            status_code=404,
            detail="Restaurante no encontrado"
        )

    db.delete(restaurant)

    db.commit()