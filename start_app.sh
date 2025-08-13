#!/bin/bash

# Script to start the Flask app with environment configuration

echo "Starting Flask app..."

# Check if virtual environment exists and activate it if it does
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Install dependencies if needed
echo "Checking dependencies..."
pip install -r requirements.txt

# Start the Flask app
echo "Starting Flask app on port 8080..."
python app.py

echo "Flask app started. Access it at http://localhost:8080"
