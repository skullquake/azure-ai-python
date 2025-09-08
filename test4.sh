#!/bin/bash
PROTOCOL=https
HOST=python-function-app-bh5xta.azurewebsites.net
HOST=python-function-app-qhm08h.azurewebsites.net
PORT=443
curl -v -X GET "$PROTOCOL://$HOST:$PORT/api/test"
