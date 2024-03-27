#!/bin/bash
# bash sript
response=$(curl -sS --compressed -o /tmp/response_body.txt -w "%{size_download}" "$1")
