help:
	@echo "---------------- HELP ---------------------" 
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/\://'| sed -e 's/##//'

setup-python:          ## Instala todas as dependências necessárias para rodar o projeto
	pip install -r requirements.txt

run:                   ## Executa a aplicação localmente
	cd ./site && python server.py