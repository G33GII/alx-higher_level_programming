#!/usr/bin/python3
"""Python Script"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status'
                                ) as response:

        content_type = type(response.read())  # Getting the type of content
        response_content = response.read()    # Reading the response content
        utf8_content = response_content.decode(
            'utf-8')  # Decoding content to UTF-8

        print("Body response:")
        # Since we are dealing with bytes
        print(f"\t- type: {response.read()}")
        print(f"\t- content: {response_content}")
        print(f"\t- utf8 content: {utf8_content}")
