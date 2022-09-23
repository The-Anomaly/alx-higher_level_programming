#!/bin/bash
# script that takes a URL, and displays all HTTP methods the server accepts
curl -sI "$1" | grep Allow | cut -d " " -f2-
