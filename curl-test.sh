#!/bin/bash

# Generate a random content for the timeline post
CONTENT=$(openssl rand -base64 10)
URL="http://127.0.0.1:5000/api/timeline_post"


create_timeline_post() {
  echo "Creating timeline post..."
  RESPONSE=$(curl -X POST -d "name=TestUser&email=test@example.com&content=$CONTENT" "$URL")
  CONTENT_CHECK=$(echo "$response" | jq -r '.content')
  echo $RESPONSE
  #curl -X POST -d "name=TestUser&email=test@example.com&content=$CONTENT" "$URL"
  echo "Timeline post created."
}

check_timeline_post() {
  echo "Checking timeline post..."
  sleep 1
  RESPONSE=$(curl -s "$URL")
  if [[ $RESPONSE == *"$CONTENT_CHECK"* ]]; then
    echo "Timeline post found."
  else
    echo "Timeline post not found."
  fi
}

delete_timeline_post() {
  echo "Deleting timeline post..."
  curl -X DELETE "$URL"
  echo "Timeline post deleted."
}

if [ "$1" == "create" ]; then
  create_timeline_post
  check_timeline_post
elif [ "$1" == "delete" ]; then
  delete_timeline_post
else
  echo "Invalid command."
fi
