FROM python:3.6.10-slim-buster

COPY . /app
WORKDIR /app

RUN pip install -U pip setuptools
RUN pip install -r requirements.txt

CMD ["python", "main.py"]