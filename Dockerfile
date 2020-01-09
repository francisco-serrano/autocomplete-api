FROM python:3.7.1 as base

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

FROM base as dev

WORKDIR /app

COPY . /app

EXPOSE 5000
