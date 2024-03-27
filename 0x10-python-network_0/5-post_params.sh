#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Variables to be sent in the POST request
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request to the URL with the specified variables using curl
# and store the response body in a variable
response_body=$(curl -sS --compressed -d "email=$email&subject=$subject" "$url")

# Display the body of the response
echo "$response_body"
