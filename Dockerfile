FROM python:3.13-alpine

WORKDIR /code
COPY requirements.txt .

RUN pip install -U pip wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY . /code

RUN ["python main.py"]