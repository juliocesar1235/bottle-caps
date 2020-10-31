FROM python:3

ENV PYTHONUNBUFFERED=1

RUN mkdir /backend-api
WORKDIR /backend-api

COPY requirements.txt /backend-api/

RUN pip install -r requirements.txt

COPY . /backend-api/