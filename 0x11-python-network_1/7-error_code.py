#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays body of the response"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        print(response.text)

    except requests.exceptions.RequestException as error:
        if 400 <= error.code:
            print("Error code: {}".format(error.code))
