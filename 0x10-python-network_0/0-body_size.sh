#!/bin/bash
# Get the URL from the command line argument


url="$1"

# Send a request to the URL using curl and store the response body in a temporary file
response=$(curl -sS --compressed -o /tmp/response_body.txt -w "%{size_download}" "$url")



# Display the size of the response body in bytes
echo "Size of the response body: $response bytes"

# Clean up temporary file
rm -f /tmp/response_body.txt
