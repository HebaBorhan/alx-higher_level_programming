#!/bin/bash
# This Script causes the server to respond with a message
curl -sL -X PUT -d "0.0.0.0:5000/catch_me" | grep -o "You got me!"
