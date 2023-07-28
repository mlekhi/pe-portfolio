#!/bin/bash

response=$(curl -X POST http://localhost:5000/api/timeline_post -d 'name=Maya&email=maya.lekhi1@gmail.com&content=testing endpoints with postman and curl.')
echo "POST response: $response"

response2=$(curl http://localhost:5000/api/timeline_post)
echo "GET response: $response2"
