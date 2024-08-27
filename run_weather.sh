#!/bin/bash

# Step 1: Install required dependencies
pip install -r requirements.txt

# Step 2: Execute the Python program with default parameters
echo -e "\nasuncion\nmetric\njson" | python3.12 main.py
