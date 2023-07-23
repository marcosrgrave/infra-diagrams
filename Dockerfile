FROM python:3.11-alpine
WORKDIR /infra-diagrams

RUN apk add --no-cache \
    graphviz \
    fontconfig \
    ttf-dejavu \
    xdg-utils

COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install --no-root --no-dev

COPY . .

CMD ["poetry", "run", "python3", "main.py"]