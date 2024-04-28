#!/usr/bin/python3
"""displays value of X-Request-Id variable in the header with requests"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
