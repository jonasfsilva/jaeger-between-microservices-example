FROM python:3.6.8-slim-jessie
LABEL maintainer="Jonas Ferreira"

ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=api.py

RUN mkdir /code
WORKDIR /code
COPY . /code

RUN pip install pipenv
RUN pipenv install --system

WORKDIR /code/app/

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]