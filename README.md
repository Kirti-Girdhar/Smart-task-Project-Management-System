# Smart Task & Project Management System

Lightweight project and task management API built with Django and Django REST Framework.

This repository implements JWT authentication, user roles, projects, tasks, comments, and attachments. The API supports filtering, searching, pagination, and Docker-based local development.

## Project Overview

Smart Task & Project Management System is an API-first backend for managing teams, projects, tasks, and collaboration. It provides authenticated endpoints for creating projects, assigning tasks, commenting, and tracking progress through a permissions-aware REST API.

### Features

- JWT authentication with token obtain/refresh flows
- User roles and profiles
- Project creation, assignment, and owner-based visibility
- Task creation, status updates, priorities, due dates, and attachments
- Commenting on tasks
- Search, filter, and pagination support on list endpoints
- Docker and docker-compose for local development
- Automated tests for API behavior and permissions

## Tech Stack

- Python 3
- Django
- Django REST Framework
- Django Filters
- SQLite (default) / PostgreSQL-compatible configuration
- Docker & docker-compose

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Kirti-Girdhar/Smart-task-Project-Management-System.git
cd "Smart task & Project Management System"
```

2. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Start the development server:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and use the API endpoints under `/api/`.

## Docker Setup

Build and run the application with Docker:

```bash
docker-compose up --build -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

To stop and remove containers:

```bash
docker-compose down
```

## Authentication

The API uses JWT authentication.

- Obtain token: `POST /api/token/`
- Refresh token: `POST /api/token/refresh/`

Example payload for token obtain:

```json
{
  "username": "youruser",
  "password": "yourpassword"
}
```

Include the access token in requests as:

```
Authorization: Bearer <access_token>
```

## API Endpoints

### Authentication

- `POST /api/token/`
- `POST /api/token/refresh/`

### Projects

- `GET /api/projects/` — List projects for authenticated user
- `POST /api/projects/` — Create a new project
- `GET /api/projects/{id}/` — Retrieve a project
- `PUT /api/projects/{id}/` — Update a project
- `DELETE /api/projects/{id}/` — Delete a project

### Tasks

- `GET /api/tasks/`
- `POST /api/tasks/`
- `GET /api/tasks/{id}/`
- `PUT /api/tasks/{id}/`
- `DELETE /api/tasks/{id}/`

### Comments

- `GET /api/comments/`
- `POST /api/comments/`
- `GET /api/comments/{id}/`
- `PUT /api/comments/{id}/`
- `DELETE /api/comments/{id}/`

> Note: The exact endpoint list may vary based on app routers and viewset configuration. Check the app URL modules in `task_manager/task_manager/urls.py` and each app folder.

## Testing

Run the full Django test suite:

```bash
python manage.py test
```

If you are using `pytest`:

```bash
pytest
```

Run a specific test module:

```bash
python manage.py test tests.test_project_api
```

## Project Structure

- `task_manager/` — Django project configuration
- `tasks/` — task management app
- `projects/` — project management app
- `users/` — custom user model and auth-related app
- `comments/` — task comments app
- `requirements.txt`, `Dockerfile`, `docker-compose.yml`

## Contributing

1. Fork the repository and create a feature branch
2. Add tests for any new behavior
3. Open a pull request with a clear description

---

If you want, I can also add example cURL requests or a Postman collection for the main API endpoints.
