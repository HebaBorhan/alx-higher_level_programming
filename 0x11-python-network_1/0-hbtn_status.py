#!/usr/bin/python3
"""Fetching with The urllib Package"""
import urllib.request as request


if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
