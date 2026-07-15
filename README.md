# Smart Task & Project Management System

Lightweight project and task management API built with Django and Django REST Framework.

This repository implements JWT authentication, user roles, projects, tasks, attachments, and filtering/pagination for APIs. It includes Docker support for easy local development.

**Highlights**
- JWT authentication (token obtain/refresh)
- Role-based users and profiles
- Projects, Tasks, Comments, and Attachments
- Filtering, searching, and pagination on list endpoints
- Docker + docker-compose for local dev

**Tech stack**: Python, Django, Django REST Framework, SQLite/PostgreSQL, Docker

---

## Quick start (local, Python)

1. Create and activate a virtualenv (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies and run migrations:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ and use the API endpoints under `/api/`.

---

## Quick start (Docker)

Build and run the services with docker-compose:

```bash
docker-compose up --build -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

To stop and remove containers:

```bash
docker-compose down
```

---

## Environment / configuration

- For local development the project uses `settings/development.py`.
- If using PostgreSQL or other services, set the appropriate `DATABASE_URL` or edit `task_manager/settings/*.py`.
- Add any sensitive values to environment variables or a `.env` file (not committed).

---

## Running tests

Run the test suite locally:

```bash
pytest
```

Or via manage.py:

```bash
python manage.py test
```

---

## Common management commands

- Apply migrations: `python manage.py migrate`
- Create admin user: `python manage.py createsuperuser`
- Collect static files (if needed): `python manage.py collectstatic --noinput`

---

## API examples

- Obtain token: `POST /api/token/` (username/password)
- List tasks: `GET /api/tasks/`
- Create task: `POST /api/tasks/`
- Update task: `PUT /api/tasks/{id}/`

Refer to the view modules under `tasks/`, `projects/`, and `users/` for the full set of endpoints.

---

## Project structure (top-level)

- `task_manager/` — Django project
- `tasks/`, `projects/`, `users/`, `comments/` — main apps
- `requirements.txt`, `docker-compose.yml`, `Dockerfile`

---

## Contributing

1. Fork the repo and create a feature branch
2. Add tests for new behavior
3. Open a pull request with a clear description

---

If you'd like, I can add a small example curl/postman collection, expand the API docs, or include environment variable examples.
