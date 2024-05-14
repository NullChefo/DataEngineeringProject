#!/bin/bash



# Build the Docker image
docker build --pull --rm -t apache-airflow:latest -f "Dockerfile" "."

