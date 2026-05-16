# Travel API

REST API for managing travel projects and places using the Art Institute of Chicago as a data source.

## Tech Stack

- Python 3.10
- Django
- Django REST Framework
- SQLite
- Docker

## Running the Project

```bash
docker-compose up -d --build
```

API will be available at `http://localhost:8000/api/`

## Documentation

- Swagger UI: `http://localhost:8000/api/docs/`
- OpenAPI schema: `http://localhost:8000/api/schema/`

## Authentication

Get a token:
```
POST /api/auth/token/
{
    "username": "your_username",
    "password": "your_password"
}
```

Include the token in every request header:
```
Authorization: Token <your_token>
```

Create a superuser:
```bash
docker-compose exec app python manage.py createsuperuser
```

## Endpoints

### Projects
| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/projects/` | List all projects |
| POST | `/api/projects/` | Create a project |
| GET | `/api/projects/{id}/` | Get a single project |
| PATCH | `/api/projects/{id}/` | Update a project |
| DELETE | `/api/projects/{id}/` | Delete a project |

### Places
| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/projects/{id}/places/` | List all places in a project |
| POST | `/api/projects/{id}/places/` | Add a place to a project |
| GET | `/api/projects/{id}/places/{id}/` | Get a single place |
| PATCH | `/api/projects/{id}/places/{id}/` | Update a place |

## Business Rules

- Maximum 10 places per project
- Cannot add the same place twice to one project
- Cannot delete a project that has visited places
- Places are validated against the Art Institute of Chicago API before saving

## Postman

Import  `docs/Travel API.yaml` from the project root into Postman to get a ready-made collection of all endpoints.
