FROM python:3.7.0

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get dist-upgrade -y \
    && apt-get install -y \
    build-essential \
    make

ADD . .

EXPOSE 5000
