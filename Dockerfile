FROM python:3.11-slim

COPY pyproject.toml poetry.lock* ./

RUN pip install poetry

RUN poetry install --no-root --no-dev

COPY . .

CMD ["poetry", "run", "uvicorn", "bundle.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]