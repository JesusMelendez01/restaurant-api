from fastapi import FastAPI

from app.database import Base, engine

from app.routers import restaurants, meals

from app.models.restaurant import Restaurant

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Restaurant API",
    version="1.0.0"
)

app.include_router(restaurants.router)

app.include_router(meals.router)


@app.get("/")
def root():

    return {
        "message": "Restaurant API funcionando"
    }