#!/bin/bash
# Check if URL argument is provided
allowed_methods=$(echo "$(curl -sS --head "$1")" | grep -i '^Allow:' | sed 's/Allow: //i')
