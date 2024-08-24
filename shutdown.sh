#!/bin/bash

PID=$(ps -ef | grep "fastapi" | grep -v "grep" | awk '{print $2}')
if [[ $PID == 0 ]]; then
  echo "FastAPIServer is already shutdown..."
  exit 0
else
  kill -9 $PID
fi

if [ $? -eq 0 ]; then
  echo "FastAPIServer shutdown successfully!"
else
  echo "FastAPIServer shutdown failed..."
fi