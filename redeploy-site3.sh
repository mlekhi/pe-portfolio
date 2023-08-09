#!/bin/bash

# change directory to project folder
cd pe-portfolio

# fetch latest changes from main branch
git fetch && git reset origin/main --hard

# activate python virtual environment
source python3-virtualenv/bin/activate

# rerun docker
docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build