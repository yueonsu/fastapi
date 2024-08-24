#!/bin/bash

PID=$(ps -ef | grep "fastapi" | grep -v "grep" | awk "{print $2}")
if [[ $PID > 0 ]]; then
  echo "FastAPIServer is already running..."
  exit 0
fi

APP_PATH=~/fastapi/
VIRTUALENV_PATH="venv"
if [ $ENV == "real" ]; then
  VIRTUALENV_PATH='virtualenv'
fi

echo "APP_PATH=$APP_PATH"
echo "VIRTUALENV_PATH=$VIRTUALENV_PATH"

source ~/$VIRTUALENV_PATH/fastapi/bin/activate
sleep 1
uvicorn main:app --host 0.0.0.0 --port 5001 > $APP_PATH/logs/system.log &

if [ $? -eq 0 ]; then
  echo "FastAPIServer Start!"
else
  echo "FastAPIServer startup failed.."
fi

deactivate