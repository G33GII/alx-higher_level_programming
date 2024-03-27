#!/bin/bash
# Check if URL argument is provided

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Send a request to the URL using curl and store the response body in a temporary file
response=$(curl -sS --compressed -o /tmp/response_body.txt -w "%{size_download}" "$url")

# Check if curl command was successful
if [ $? -ne 0 ]; then
    echo "Failed to fetch URL: $url"
    exit 1
fi

# Display the size of the response body in bytes
echo "Size of the response body: $response bytes"

# Clean up temporary file
rm -f /tmp/response_body.txt
