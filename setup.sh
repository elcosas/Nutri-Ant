#!/bin/env bash

python3 -m venv .venv
source .venv/bin/activate
.venv/bin/python3 -m pip install -r requirements.txt

# To test if it works, cd into app and type: flask run
# This should work and not break