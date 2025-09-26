# 🚀 Quick Start Guide

## Prerequisites
- Python 3.11+
- Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

## Setup Steps

### 1. Environment Setup
```bash
# Copy environment template
cp env.example .env

# Edit .env and add your Gemini API key
# GEMINI_API_KEY=your_actual_api_key_here
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the Application

#### Option A: Using Startup Scripts
```bash
# Linux/Mac
chmod +x start.sh
./start.sh

# Windows
start.bat
```

#### Option B: Manual Start
```bash
# Terminal 1: Start backend
cd backend
python main.py

# Terminal 2: Start CLI
python cli.py
```

#### Option C: Docker
```bash
docker-compose up --build
```

## 🧪 Testing

Run the test suite:
```bash
python test.py
```

## 📋 Usage

1. **Start the CLI**: Run `python cli.py`
2. **Choose option 1**: Conduct Research
3. **Enter your topic**: e.g., "artificial intelligence"
4. **Wait for results**: The agents will work together to research and format your query
5. **View history**: Choose option 2 to see past research

## 🔧 API Usage

The backend also exposes a REST API:

```bash
# Health check
curl http://localhost:8000/health

# Research query
curl -X POST "http://localhost:8000/research" \
     -H "Content-Type: application/json" \
     -d '{"query": "machine learning"}'
```

## 🐛 Troubleshooting

- **API Key Error**: Make sure your Gemini API key is correctly set in `.env`
- **Connection Failed**: Ensure the backend is running on port 8000
- **Import Errors**: Run `pip install -r requirements.txt`

## 📚 Example Queries

Try these research topics:
- "artificial intelligence"
- "climate change" 
- "quantum computing"
- "renewable energy"
- "space exploration"
