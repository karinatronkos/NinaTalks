FROM python:3.7.0

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get dist-upgrade -y \
    && apt-get install -y \
    build-essential

ADD site .
ADD requirements.txt .
ADD Makefile .

EXPOSE 5000
