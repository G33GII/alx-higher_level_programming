#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Send a GET request to the URL with the header variable X-School-User-Id set to 98 using curl
# and store the response body in a variable
response_body=$(curl -sS --compressed -H "X-School-User-Id: 98" "$url")

# Display the body of the response
echo "$response_body"
