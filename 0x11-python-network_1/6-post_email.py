#!/usr/bin/python3
"""sends a POST request to the passed URL with the email
and displays body of the response (decoded in utf-8) with requests"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    Mail = {"email": sys.argv[2]}

    req = requests.post(url, Mail)

    print(req.text)
