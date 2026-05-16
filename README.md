# Restaurant API - FastAPI

API REST desarrollada con FastAPI para la gestión de restaurantes y consumo de la API externa TheMealDB.

---

# Características

- CRUD completo de restaurantes
- Integración con API externa TheMealDB
- Validaciones con Pydantic
- Base de datos SQLite
- Tests con pytest
- Documentación automática con Swagger
- Docker support

---

# Tecnologías utilizadas

- Python 3.11+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- httpx
- pytest
- Docker

---

# Instalación

## 1. Clonar repositorio

```bash
git clone https://github.com/TU_USUARIO/restaurant-api.git
2. Entrar al proyecto
cd restaurant-api
3. Crear entorno virtual
Windows
python -m venv venv
Linux / Mac
python3 -m venv venv
4. Activar entorno virtual
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
5. Instalar dependencias
pip install -r requirements.txt
Ejecutar el proyecto
uvicorn app.main:app --reload

La API estará disponible en:

http://localhost:8000
Swagger Documentation

FastAPI genera documentación automática.

Abrir:

http://localhost:8000/docs
Base de Datos

Se utiliza SQLite.

El archivo de base de datos se genera automáticamente:

restaurants.db
Endpoints
Root
GET /

Retorna mensaje de prueba.

Response
{
  "message": "Restaurant API funcionando"
}
Restaurants
POST /api/restaurants/

Crear restaurante.

Request
{
  "name": "Tacos El Patron",
  "address": "Av. Mexico 123",
  "city": "Guadalajara",
  "cuisine_type": "Mexicana",
  "rating": 4.5,
  "is_active": true
}
Response
{
  "id": 1,
  "name": "Tacos El Patron",
  "address": "Av. Mexico 123",
  "city": "Guadalajara",
  "cuisine_type": "Mexicana",
  "rating": 4.5,
  "is_active": true,
  "created_at": "2026-05-13T12:00:00"
}
GET /api/restaurants/

Obtener todos los restaurantes.

Query params opcionales
Parámetro	Tipo	Descripción
city	string	Filtrar por ciudad
is_active	boolean	Filtrar por estado
Ejemplo
/api/restaurants/?city=Guadalajara
GET /api/restaurants/{id}

Obtener restaurante por ID.

Response 200
{
  "id": 1,
  "name": "Tacos El Patron",
  "address": "Av. Mexico 123",
  "city": "Guadalajara",
  "cuisine_type": "Mexicana",
  "rating": 4.5,
  "is_active": true,
  "created_at": "2026-05-13T12:00:00"
}
Response 404
{
  "detail": "Restaurante no encontrado"
}
PUT /api/restaurants/{id}

Actualizar restaurante parcialmente.

Request
{
  "rating": 5.0,
  "is_active": false
}
DELETE /api/restaurants/{id}

Eliminar restaurante.

Response
204 No Content
Meals API
GET /api/meals/search?name={meal}

Buscar comidas usando TheMealDB.

Ejemplo
/api/meals/search?name=chicken
Response
{
  "results": [
    {
      "id": "52772",
      "name": "Teriyaki Chicken Casserole",
      "category": "Chicken",
      "cuisine": "Japanese"
    }
  ]
}
Ejecutar tests
pytest
Resultado esperado
2 passed
Docker
Construir imagen
docker build -t restaurant-api .
Ejecutar contenedor
docker run -p 8000:8000 restaurant-api
Estructura del proyecto
restaurant-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── dependencies.py
│   │
│   ├── models/
│   │   └── restaurant.py
│   │
│   ├── schemas/
│   │   └── restaurant.py
│   │
│   ├── routers/
│   │   ├── restaurants.py
│   │   └── meals.py
│   │
│   └── services/
│       └── mealdb_client.py
│
├── tests/
│   └── test_restaurants.py
│
├── requirements.txt
├── Dockerfile
├── pytest.ini
├── README.md
└── .gitignore
Validaciones implementadas
Nombre obligatorio
Rating entre 0.0 y 5.0
Manejo de errores HTTP
Validación automática con Pydantic
Tests implementados
Test endpoint raíz
Test listado de restaurantes
Autor

Desarrollado como prueba técnica para desarrollador Python Junior.