#!/bin/bash
# script that sends a JSON POST request and displays the response
curl -s -d @"$2" -H "Content-Type: application/json" "$1" -X POST
