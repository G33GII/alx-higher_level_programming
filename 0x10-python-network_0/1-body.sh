#!/bin/bash
# Check if URL argument is provided
response_body=$(curl -sS --compressed -w "%{http_code}" "$1")
