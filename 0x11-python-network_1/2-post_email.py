#!/usr/bin/python3
"""sends a POST request to the passed URL with the email
and displays body of the response (decoded in utf-8)"""
import urllib.request as request
import urllib.parse as parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    Mail = {"email": sys.argv[2]}

    data = parse.urlencode(Mail).encode("utf-8")

    with request.urlopen(url, data) as response:
        decoded_body = response.read().decode("utf-8")
        print(decoded_body)
