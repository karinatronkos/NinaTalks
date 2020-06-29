#!/bin/bash

source .env;
echo "GCP PROJECT ID: ";
echo $GCP_PROJECT_ID;
echo " ";

echo " ";
echo " ";
echo "Definir as opções ID do projeto e zona do Compute Engine"
echo " ";
echo " ";
gcloud config set project $GCP_PROJECT_ID;
gcloud config set compute/zone us-central1-c;

echo " ";
echo " ";
echo "Criando um cluster de 3 nós chamado hello-cluster"
echo " ";
echo " ";
gcloud container clusters create ninatalks-cluster --num-nodes=3;
