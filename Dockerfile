FROM docker.io/library/python:3.10-slim

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . .

RUN poetry run python3 manage.py makemigrations

RUN poetry run python3 manage.py migrate

RUN DJANGO_SUPERUSER_PASSWORD=admin poetry run python3 manage.py createsuperuser --username admin --email admin@example.com --noinput

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["poetry", "run", "python3", "manage.py", "runserver", "0.0.0.0:8000"]
