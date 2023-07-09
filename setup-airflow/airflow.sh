#!bin/sh

# get file
wget https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml

# create necessary directories
mkdir ./dags ./plugins ./logs

# create an .env file to assign the current user ID
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

# up airflow-init
docker compose up airflow-init

# up all airflow containers
docker compose up -d