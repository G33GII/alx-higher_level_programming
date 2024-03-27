#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Send a GET request to the URL using curl and store the response body in a variable
response_body=$(curl -sS --compressed -w "%{http_code}" "$url")

# Get the status code from the end of the response
status_code=${response_body: -3}

# Check if the status code is 200 (OK)
if [ "$status_code" = "200" ]; then
    # Display the body of the response
    echo "${response_body:0:${#response_body}-3}"
else
    # Display an error message if the status code is not 200
    echo "Error: Received status code $status_code"
fi
