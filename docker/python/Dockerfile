FROM python:3.12.7

WORKDIR /tomiko_trade

COPY ./tomiko_trade /tomiko_trade

RUN pip install --no-cache-dir -r /tomiko_trade/requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
