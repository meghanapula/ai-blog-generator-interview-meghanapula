#!/bin/bash

KEYWORD="wireless earbuds"
DATE=$(date +%Y%m%d)
ENCODED_KEYWORD=$(echo "$KEYWORD" | sed 's/ /%20/g')
FILENAME="posts/${KEYWORD// /_}_$DATE.json"

curl -s "http://localhost:5000/generate?keyword=${ENCODED_KEYWORD}" -o $FILENAME
