#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}

    # Encode the email as a parameter
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    # Send a POST request to the URL with the email as a parameter
    combo = urllib.request.Request(url, data)
    with urllib.request.urlopen(combo) as response:
        # Read and decode the body of the response in utf-8
        body = response.read().decode('utf-8')
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print(request_id)
