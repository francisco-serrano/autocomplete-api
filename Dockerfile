FROM python:3.7.1 as base

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

FROM base as dev

WORKDIR /app

#ENV ELASTICSEARCH_HOST es01
#ENV ELASTICSEARCH_PORT 9200
#ENV BASE_JSON_DIR /app/sample_conversations.json
#ENV FLASK_APP /app/app.py

COPY . /app

EXPOSE 5000
