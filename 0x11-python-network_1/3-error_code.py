#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays body of the response"""
import urllib.request as request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as error:
        print("Error code: ", error.code)
