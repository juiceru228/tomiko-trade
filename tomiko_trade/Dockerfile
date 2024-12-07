FROM postgres-17.2-alpine
COPY ./tomiko_trade/database/dump.sql ./docker-entrypoint-initdb.d/

FROM python:3.12.7-alpine

WORKDIR /app

RUN apk add --no-cache postgresql-client

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:4000"]

