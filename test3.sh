#!/bin/bash
PROTOCOL=https
HOST=main-pnp-linux-function-app3.azurewebsites.net
HOST=python-function-app-bh5xta.azurewebsites.net
HOST=python-function-app-qhm08h.azurewebsites.net
PORT=443
curl -v -X POST "$PROTOCOL://$HOST:$PORT/api/callai" \
  -F "header=Test Header" \
  -F "subject=Test Subject" \
  -F "recipient=test@example.com" \
  -F "body=This is a test email body." \
  -F "attachments=@/mnt/c/tmp/a.pdf"
