#!/bin/bash
# Bash script displaying the size of body of URL
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
