#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Send an OPTIONS request to the URL using curl and store the response headers in a variable
response_headers=$(curl -sS --head "$url")

# Extract the Allow header which contains the allowed HTTP methods
allowed_methods=$(echo "$response_headers" | grep -i '^Allow:' | sed 's/Allow: //i')

# Display the allowed HTTP methods
echo "Allowed HTTP methods for $url: $allowed_methods"
