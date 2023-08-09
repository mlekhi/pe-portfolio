#!/bin/bash

# change directory to project folder
cd pe-portfolio

# fetch latest changes from main branch
git fetch && git reset origin/main --hard

# rerun docker
docker compose -f docker-compose.prod.yml down

# Remove the mysql container specifically
docker rm mysql

docker compose -f docker-compose.prod.yml up -d --build