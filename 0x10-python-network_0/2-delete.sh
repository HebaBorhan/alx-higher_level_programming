#!/bin/bash
# This Script sends DELETE request to URL passed as the first argument and displays the body of the response
curl -s -X DELETE "$1"
