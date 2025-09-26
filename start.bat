@echo off

REM AI Research Assistant Startup Script for Windows

echo 🤖 AI Research Assistant Setup
echo ================================

REM Check if .env file exists
if not exist .env (
    echo 📝 Creating .env file from template...
    copy env.example .env
    echo ⚠️  Please edit .env file and add your GEMINI_API_KEY
    echo    Get your API key from: https://makersuite.google.com/app/apikey
    pause
)

REM Check if virtual environment exists
if not exist venv (
    echo 🐍 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt

REM Start backend
echo 🚀 Starting backend server...
cd backend
start /B python main.py

REM Wait for backend to start
echo ⏳ Waiting for backend to start...
timeout /t 5 /nobreak >nul

REM Start CLI
echo 🎯 Starting CLI interface...
cd ..
python cli.py

echo 👋 Goodbye!
pause
