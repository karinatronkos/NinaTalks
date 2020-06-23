help:
	@echo "---------------- HELP ---------------------" 
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/\://'| sed -e 's/##//'

setup-python:       ## Instala todas as dependências necessárias para rodar o projeto
	pip install -r requirements.txt

run-web:                ## Executa a aplicação web localmente
	cd ./site && python server.py

run-admin:              ## Executa a aplicação do administrador localmente
	cd ./admin && python server.py

up:		   ## Executa a aplicação via docker compose
	docker-compose up --force-recreate