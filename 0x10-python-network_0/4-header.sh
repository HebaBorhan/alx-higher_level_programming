#!/bin/bash
# This Script takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -s -L -H "X-School-User-Id: 98" "$1"
