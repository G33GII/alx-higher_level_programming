#!/bin/bash
# Bash script
curl -s -o /dev/null -w "%{http_code}" "$1"
