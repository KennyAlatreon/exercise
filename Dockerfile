FROM python:3.7-alpine
MAINTAINER KennyAlatreon <kennyweb1337@gmail.com>

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN python manage.py makemigrations
RUN python manage.py migrate


RUN adduser -D user
USER user
