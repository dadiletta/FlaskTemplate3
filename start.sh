#!/bin/bash

# Find the latest Python 3 version available on the system
if command -v python3.11 &> /dev/null; then
  PYTHON="python3.11"
elif command -v python3.10 &> /dev/null; then
  PYTHON="python3.10"
elif command -v python3.9 &> /dev/null; then
  PYTHON="python3.9"
elif command -v python3.8 &> /dev/null; then
  PYTHON="python3.8"
elif command -v python3.7 &> /dev/null; then
  PYTHON="python3.7"
elif command -v python3 &> /dev/null; then
  PYTHON="python3"
else
  echo "Error: Python 3 not found"
  exit 1
fi

# Print the Python version being used
echo "Using $PYTHON version:"
$PYTHON -V

# Install requirements from requirements.txt
$PYTHON -m pip install -r requirements.txt

# Additionally ensure gunicorn is installed (in case it's not in requirements.txt)
$PYTHON -m pip install gunicorn

# Start the Flask application using gunicorn
$PYTHON -m gunicorn --bind 0.0.0.0:5000 main:app