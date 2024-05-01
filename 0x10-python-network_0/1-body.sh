#!/bin/bash
# This Script takes in a URL, sends a GET request to it, and displays the body of the response
curl -s "$1" | grep -oP "(?<=^HTTP\/1\.1 200 OK\r\n\r\n).*"
