#!/bin/bash
PROTOCOL=http
HOST=localhost
PORT=7071
curl -v -X GET "$PROTOCOL://$HOST:$PORT/api/test"
