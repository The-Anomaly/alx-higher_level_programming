#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me and display the server message
curl -sL -d "user_id=98" -H "origin: HolbertonSchool" "0.0.0.0:5000/catch_me" -X PUT
