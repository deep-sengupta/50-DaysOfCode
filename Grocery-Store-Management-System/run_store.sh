#!/bin/bash

if command -v python3 &>/dev/null; then
    echo "Running Grocery Store Management System..."
    python3 main.py
else
    echo "Python3 is not installed. Please install Python3 to run this program."
fi