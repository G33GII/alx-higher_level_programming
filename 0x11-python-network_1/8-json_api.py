#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    # Set the default value for the letter parameter
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    # Send a POST request to the specified URL with the letter as a parameter
    response = requests.post(
        'http://0.0.0.0:5000/search_user', data={'q': letter})

    try:
        # Parse the response as JSON
        data = response.json()

        # Check if the JSON response is not empty and properly formatted
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
