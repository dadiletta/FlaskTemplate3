#!/bin/bash

# Create a temporary virtual environment
python -m venv freeze-env

# Activate the virtual environment
source freeze-env/bin/activate

# Install all dependencies from requirements.txt except werkzeug
pip install -r requirements.txt

# Downgrade dependencies for freeze
pip install -r freeze-requirements.txt

# Run the freeze script
python freeze.py

# Deactivate and remove the virtual environment
deactivate
rm -rf freeze-env