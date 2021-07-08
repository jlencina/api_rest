FROM python:3.8

WORKDIR /fastapi-app

COPY requeriments.txt .

RUN pip install  -r requeriments.txt

COPY ./app ./app

CMD ["python3", "./app/main.py"]
