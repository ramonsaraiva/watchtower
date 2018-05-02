FROM python:3.7.0b3-stretch

COPY . /app
WORKDIR /app

ENV FLASK_ENV docker
ENV FLASK_APP watchtower.application

COPY ./requirements/docker.txt requirements/docker.txt
RUN pip install -r requirements/docker.txt