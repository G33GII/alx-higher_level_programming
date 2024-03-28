#!/usr/bin/python3
"""Python Script"""

import urllib.request
import sys

if __name__ == "__main__":
    # Check if the script has been provided with a URL argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Send a request to the URL
    with urllib.request.urlopen(url) as response:
        # Check if the 'X-Request-Id' header is present in the response
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print(f"Value of X-Request-Id variable: {request_id}")
        else:
            print("X-Request-Id header not found in the response.")
