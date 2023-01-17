#!/bin/bash
# Display all HTTP methods the server will accept
curl -isLX "$1" | grep 'Allow' | cut -f2- -d' '
