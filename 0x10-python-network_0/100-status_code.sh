#!/bin/bash
# script that takes a URl, sends a request and displays the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
