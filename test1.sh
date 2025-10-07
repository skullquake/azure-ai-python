#!/bin/bash
PROTOCOL=http
HOST=localhost
PORT=7071
curl -s -X POST "$PROTOCOL://$HOST:$PORT/api/callai" \
  -F "header=qwerasdfzxcv Test Header" \
  -F "subject=qwerasdfzxcv Test Subject" \
  -F "recipient=qwerasdfzxcv@example.com" \
  -F "body=qwerasdfzxcv This is a test email body." \
  -F "attachments=@/mnt/c/tmp/invoice.png"
