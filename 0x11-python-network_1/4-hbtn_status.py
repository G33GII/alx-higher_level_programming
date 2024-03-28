#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    # Send a GET request to the URL
    response = requests.get(url)

    # Display the body of the response with tabulation before each line
    print("- body response:")
    for line in response.text.split('\n'):
        print(f"\t- {line}")
