FROM python:3.7.0

# Dependencias de Ambiente
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get dist-upgrade -y \
    && apt-get install -y \
    build-essential \
    make

# Clonando o código fonte do projeto
ADD ninatalks/ /usr/local/src/
ADD requirements.txt /usr/local/src/
ADD Makefile /usr/local/src/

WORKDIR /usr/local/src/

# Dependencias do projeto
RUN make setup-python
RUN pip install gunicorn

# Preparando para a execução
ENV PORT 8080

# Execução do projeto
CMD gunicorn --bind 0.0.0.0:$PORT server:app
