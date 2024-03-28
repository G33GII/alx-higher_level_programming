#!/usr/bin/python3

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read().decode('utf-8')
        for char in html:
            print(f"{char}: {ord(char)}")
