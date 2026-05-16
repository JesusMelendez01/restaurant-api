from fastapi import APIRouter, HTTPException

from app.services.mealdb_client import search_meals

router = APIRouter(
    prefix="/api/meals",
    tags=["Meals"]
)


@router.get("/search")
async def search_meal(name: str):

    try:
        return await search_meals(name)

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Error consultando TheMealDB"
        )