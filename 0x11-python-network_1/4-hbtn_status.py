#!/usr/bin/python3
"""Fetching status with The requests Package"""
import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    html = response.text
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
