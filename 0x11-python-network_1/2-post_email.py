#!/usr/bin/python3
"""sends a POST request to the passed URL with the email
and displays the body of the response (decoded in utf-8)"""
import urllib.request as request
import urllib.parse as parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email}).encode()

    with request.urlopen(url, data) as response:
        decoded_body = response.read().decode("utf-8")
        print(decoded_body)
