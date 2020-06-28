IMAGE_GCP_PATH=gcr.io/sixth-impulse-281502/flask-fire

help:
	@echo "---------------- HELP ---------------------" 
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/\://'| sed -e 's/##//'

setup-python:       	## Instala todas as dependências necessárias para rodar o projeto
	pip install -r requirements.txt

run-web:           	## Executa a aplicação web localmente
	cd ./site && python server.py

run-admin:          	## Executa a aplicação do administrador localmente
	cd ./admin && python server.py

up:		   	## Executa a aplicação via docker compose
	docker-compose up --force-recreate

create-gcp-enviroment: 	## Cria ambiente no GCP
	bash scripts/create_gcp_enviroment.sh

image-push: 		## Envia imagem base docker para o GCP
	gcloud builds submit --tag ${IMAGE_GCP_PATH}:v1

image-build: 		## Build imagem base docker para o GCP
	docker build -t ${IMAGE_GCP_PATH}:v1 .

image-run: 		## Roda imagem base docker para o GCP
	docker run -p 8080:8080 -it ${IMAGE_GCP_PATH}:v1

deploy:			## Deploy da imagem para o cluster kubernetes no GCP
	kubectl create deployment hello-web --image=${IMAGE_GCP_PATH}:v1
