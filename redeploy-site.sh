#!/bin/bash

tmux kill-session -a
tmux kill-session -t pe-portfolio

cd pe-portfolio

git fetch && git reset origin/main --hard

source ./python3-virtualenv/bin/activate
pip install -r requirements.txt

tmux new-session -d -s pe-portfolio
tmux send-keys -t pe-portfolio 'cd pe-portfolio' Enter
tmux send-keys -t pe-portfolio 'source /python3-virtualenv/bin/activate' Enter
tmux send-keys -t pe-portfolio 'flask run --host=24.199.97.117' Enter
