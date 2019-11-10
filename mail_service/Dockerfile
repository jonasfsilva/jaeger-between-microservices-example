FROM python:3.6.8-slim-jessie
LABEL maintainer="Jonas Ferreira"

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code

RUN pip install pipenv
RUN pipenv install --system

WORKDIR /code/app/

CMD [ "python", "main.py" ]