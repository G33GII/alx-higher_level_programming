#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    # Get URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Data to be sent in the POST request
    data = {'email': email}

    # Send a POST request to the URL with the email as a parameter
    response = requests.post(url, data=data)

    # Display the body of the response
    print("Your email is:", response.text)