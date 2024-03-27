#!/bin/bash
# Check if URL argument is provided
response_body=$(curl -sS --compressed -X DELETE "$1")
