#!/usr/bin/python3
"""Fetching status with The requests Package"""
import requests


if __name__ == "__main__":
    with requests.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
