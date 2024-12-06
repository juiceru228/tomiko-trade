FROM postgres
COPY ./tomiko_trade/database/dump.sql ./docker-entrypoint-initdb.d/

FROM python:3.12.7

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:4000"]

