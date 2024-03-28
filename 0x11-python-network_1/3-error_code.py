#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        # Send a request to the URL
        with urllib.request.urlopen(url) as response:
            # Read and decode the body of the response in utf-8
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors
        print(f"Error code: {e.code}")
