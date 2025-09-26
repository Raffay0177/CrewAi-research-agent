# 🤖 AI Research Assistant

An end-to-end AI Research Assistant built with **CrewAI** and **Gemini API**, featuring multiple AI agents that work together to conduct comprehensive research on any topic.

## 🏗️ Architecture

The system uses a multi-agent approach with three specialized AI agents:

1. **🔍 Searcher Agent** - Finds relevant information using web search capabilities
2. **📝 Summarizer Agent** - Condenses findings into organized bullet points  
3. **✅ Verifier Agent** - Fact-checks and formats results into professional reports

## 🚀 Features

- **Multi-Agent Research**: Three specialized AI agents working in sequence
- **Gemini API Integration**: Powered by Google's Gemini Pro model
- **FastAPI Backend**: RESTful API with automatic documentation
- **CLI Interface**: Easy-to-use command-line interface for testing
- **Docker Support**: Containerized deployment with Docker Compose
- **Research History**: Track and view past research queries
- **Mock Web Search**: Simulated search results for demonstration

## 📋 Prerequisites

- Python 3.11+
- Docker and Docker Compose (optional)
- Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

## 🛠️ Installation

### Option 1: Local Development

1. **Clone and setup**:
   ```bash
   git clone <repository-url>
   cd ai-research-assistant
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**:
   ```bash
   cp env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

4. **Start the backend**:
   ```bash
   cd backend
   python main.py
   ```

5. **Run the CLI** (in a new terminal):
   ```bash
   python cli.py
   ```

### Option 2: Docker Deployment

1. **Setup environment**:
   ```bash
   cp env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

2. **Start with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

## 🎯 Usage

### CLI Interface

The CLI provides an interactive interface with the following options:

1. **🔍 Conduct Research** - Enter a topic and get a comprehensive research report
2. **📚 View Research History** - See all your past research queries
3. **❌ Exit** - Close the application

### API Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `POST /research` - Conduct research on a topic

#### Example API Usage

```bash
curl -X POST "http://localhost:8000/research" \
     -H "Content-Type: application/json" \
     -d '{"query": "artificial intelligence"}'
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional (for future enhancements)
# OPENAI_API_KEY=your_openai_key_here
# SERPAPI_API_KEY=your_serpapi_key_here
```

### Customizing Agents

You can modify the agent configurations in `backend/main.py`:

- **Searcher Agent**: Modify search behavior and tools
- **Summarizer Agent**: Adjust summarization style and format
- **Verifier Agent**: Change fact-checking criteria and report format

## 📁 Project Structure

```
ai-research-assistant/
├── backend/
│   ├── main.py              # FastAPI application with CrewAI agents
│   └── Dockerfile           # Backend container configuration
├── cli.py                   # CLI interface for testing
├── requirements.txt         # Python dependencies
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile              # CLI container configuration
├── env.example             # Environment variables template
└── README.md               # This file
```

## 🔍 How It Works

1. **User Input**: User provides a research query via CLI or API
2. **Searcher Agent**: Uses web search tools to gather information
3. **Summarizer Agent**: Processes and organizes the findings
4. **Verifier Agent**: Fact-checks and formats the final report
5. **Output**: Returns a comprehensive research report

## 🧪 Testing

### Manual Testing

1. Start the backend server
2. Run the CLI interface
3. Try different research queries:
   - "artificial intelligence"
   - "climate change"
   - "quantum computing"

### API Testing

```bash
# Health check
curl http://localhost:8000/health

# Research query
curl -X POST "http://localhost:8000/research" \
     -H "Content-Type: application/json" \
     -d '{"query": "machine learning"}'
```

## 🚀 Future Enhancements

- **Real Web Search**: Integrate with actual search APIs (SerpAPI, Google Search)
- **Database Storage**: Persist research history in a database
- **Web Frontend**: Add a React-based web interface
- **Advanced Agents**: Add more specialized agents (translator, analyst, etc.)
- **Export Options**: PDF, Word, or Markdown export
- **Collaborative Research**: Multi-user research sessions

## 🐛 Troubleshooting

### Common Issues

1. **API Connection Failed**:
   - Ensure the backend is running on port 8000
   - Check your Gemini API key is valid

2. **Docker Issues**:
   - Make sure Docker is running
   - Check if ports 8000 is available

3. **Import Errors**:
   - Verify all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version (3.11+ required)

### Logs

- Backend logs: Check terminal where `python main.py` is running
- Docker logs: `docker-compose logs backend`

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Built with ❤️ using CrewAI, Gemini API, and FastAPI**
