#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Send a DELETE request to the URL using curl and store the response body in a variable
response_body=$(curl -sS --compressed -X DELETE "$url")

# Display the body of the response
echo "$response_body"
