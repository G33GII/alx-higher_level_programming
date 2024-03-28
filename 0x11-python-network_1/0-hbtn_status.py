#!/usr/bin/python3
"""Python Script"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status'
                                ) as response:
        # Read the response content only once
        response_content = response.read()

        """Get the charset from the response headers,
        defaulting to 'utf-8' if not found"""
        charset = response.headers.get_content_charset(failobj='utf-8')

        # Decode the content using the charset
        utf8_content = response_content.decode(charset)

        print("Body response:")
        print(f"    - type: bytes")  # Since we are dealing with bytes
        print(f"    - content: {response_content}")
        print(f"    - utf8 content: {utf8_content}")
