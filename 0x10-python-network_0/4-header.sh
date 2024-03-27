#!/bin/bash
# Check if URL argument is provided
response_body=$(curl -sS --compressed -H "X-School-User-Id: 98" "$1")
