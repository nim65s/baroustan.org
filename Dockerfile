FROM python:3.9-slim as build

WORKDIR /app

RUN apt-get update -q && apt-get install -qqy git \
 && pip install poetry

ADD pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false --local \
 && poetry install --no-dev --no-root --no-interaction --no-ansi

ADD . .

RUN pelican

FROM nim65s/ndh

COPY --from=build /app/output /srv
