#!/bin/bash

# Service name provided as a variable
SERVICE_NAME="danalyzerd"

# Get the PID of the process
PID=$(ps -aux | grep "$SERVICE_NAME" | grep -v grep | awk '{print $2}')

# Check if a PID was found
if [ -z "$PID" ]; then
  echo "No process found for service: $SERVICE_NAME"
  exit 1
fi

# Kill the process
echo "Killing process with PID: $PID"
kill -9 $PID

# Verify if the process was killed
if [ $? -eq 0 ]; then
  echo "Process $PID killed successfully."
else
  echo "Failed to kill process $PID."
fi
