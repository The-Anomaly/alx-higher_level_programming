#!/bin/bash
# script that takes a URL, sends a POST request and displays the body of the response
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1" -X POST
