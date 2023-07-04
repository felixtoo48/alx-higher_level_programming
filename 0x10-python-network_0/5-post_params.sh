#!/bin/bash
# sends a post request to passed URL and display body of response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
