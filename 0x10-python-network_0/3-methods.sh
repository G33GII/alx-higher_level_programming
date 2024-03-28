#!/bin/bash
# Check if URL argument is provided
curl -sS --head "$1")" | grep -i '^Allow:' | sed 's/Allow: //i'
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
