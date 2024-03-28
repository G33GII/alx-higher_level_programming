#!/bin/bash
# Bash script
curl  -o /dev/null -sw "%{http_code}" $1
