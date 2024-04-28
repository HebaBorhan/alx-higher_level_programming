#!/usr/bin/python3
"""displays value of X-Request-Id variable in the header of the response"""
import urllib.request as request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as responce:
        print(responce.headers['X-Request-Id'])
