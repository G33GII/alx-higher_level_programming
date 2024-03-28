#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    # Assume URL is provided as a command-line argument
    url = sys.argv[1]

    # Send a request to the URL
    response = requests.get(url)

    # Check if 'X-Request-Id' is present in the response headers
    if 'X-Request-Id' in response.headers:
        request_id = response.headers['X-Request-Id']
        print(f"Value of X-Request-Id variable: {request_id}")
    else:
        print("X-Request-Id header not found in the response.")
