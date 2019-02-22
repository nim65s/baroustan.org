FROM alpine:3.9 as build

RUN mkdir /app
WORKDIR /app

RUN apk update -q && apk add -q --no-cache \
    git \
    py3-pillow \
 && pip3 install --no-cache-dir -U pip \
 && pip3 install --no-cache-dir \
    pipenv

ADD Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

ADD . .

ARG DOMAIN_NAME=localhost

RUN pelican

FROM nim65s/ndh:nginx

COPY --from=build /app/output /srv
