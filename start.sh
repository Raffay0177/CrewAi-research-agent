#!/bin/bash

# AI Research Assistant Startup Script

echo "🤖 AI Research Assistant Setup"
echo "================================"

# Check if .env file exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp env.example .env
    echo "⚠️  Please edit .env file and add your GEMINI_API_KEY"
    echo "   Get your API key from: https://makersuite.google.com/app/apikey"
    read -p "Press Enter after adding your API key..."
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🐍 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Start backend
echo "🚀 Starting backend server..."
cd backend
python main.py &
BACKEND_PID=$!

# Wait for backend to start
echo "⏳ Waiting for backend to start..."
sleep 5

# Start CLI
echo "🎯 Starting CLI interface..."
cd ..
python cli.py

# Cleanup
echo "🛑 Shutting down..."
kill $BACKEND_PID 2>/dev/null
echo "👋 Goodbye!"
