FROM python:alpine3.7 as build

RUN mkdir /app
WORKDIR /app

ADD Pipfile Pipfile.lock ./

RUN apk update -q && apk add -q --no-cache \
    git \
    py3-pillow \
 && pip3 install --no-cache-dir -U pip \
 && pip3 install --no-cache-dir \
    pipenv \
 && pipenv install --system --deploy --pre

ENV PYTHONPATH=/usr/lib/python3.6/site-packages

ADD . .

ARG DOMAIN_NAME=local

RUN pelican

FROM nim65s/ndh:nginx

COPY --from=build /app/output /srv
