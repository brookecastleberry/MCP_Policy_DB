#!/bin/bash

# Script to start the Flask app with environment configuration

echo "Starting Flask app..."

# Check if virtual environment exists, create it if it doesn't
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating new virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created successfully."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies if needed
echo "Checking dependencies..."
pip install -r requirements.txt

# Start the Flask app
echo "Starting Flask app on port 8080..."
python app.py

echo "Flask app started. Access it at http://localhost:8080"
