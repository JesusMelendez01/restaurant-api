import httpx

BASE_URL = "https://www.themealdb.com/api/json/v1/1"


async def search_meals(name: str):

    url = f"{BASE_URL}/search.php?s={name}"

    async with httpx.AsyncClient(timeout=10.0) as client:

        response = await client.get(url)

        response.raise_for_status()

        data = response.json()

        meals = data.get("meals") or []

        return {
            "results": [
                {
                    "id": meal["idMeal"],
                    "name": meal["strMeal"],
                    "category": meal["strCategory"],
                    "cuisine": meal["strArea"]
                }
                for meal in meals
            ]
        }
