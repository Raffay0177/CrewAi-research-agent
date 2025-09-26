from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai.tools import BaseTool
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# Load environment variables
load_dotenv()

app = FastAPI(title="AI Research Assistant", version="1.0.0")

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY", "demo_key")
if api_key == "demo_key":
    print("⚠️  WARNING: Using demo mode. Please set GEMINI_API_KEY in .env file for full functionality")
    # Use a mock model for demo
    model = None
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

class ResearchRequest(BaseModel):
    query: str

class ResearchResponse(BaseModel):
    query: str
    report: str
    timestamp: str
    sources: List[str]

# Custom Web Search Tool
class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = "Search the web for information about a given topic"
    
    def _run(self, query: str) -> str:
        """Mock web search - in production, integrate with real search API"""
        # Mock search results for demonstration
        mock_results = {
            "artificial intelligence": [
                "AI is transforming industries worldwide with machine learning and deep learning technologies.",
                "Recent advances in large language models have revolutionized natural language processing.",
                "AI applications include healthcare, finance, autonomous vehicles, and robotics."
            ],
            "climate change": [
                "Climate change refers to long-term shifts in global temperatures and weather patterns.",
                "Human activities, particularly greenhouse gas emissions, are the primary driver of recent climate change.",
                "Effects include rising sea levels, extreme weather events, and ecosystem disruptions."
            ],
            "quantum computing": [
                "Quantum computing uses quantum mechanical phenomena to process information.",
                "Quantum computers could potentially solve certain problems exponentially faster than classical computers.",
                "Major challenges include quantum decoherence and error correction."
            ]
        }
        
        # Find best matching topic or return general results
        query_lower = query.lower()
        for topic, results in mock_results.items():
            if any(word in query_lower for word in topic.split()):
                return "\n".join(results)
        
        return "No specific information found. Please try a different query or be more specific about your research topic."

# Initialize CrewAI Agents
def create_agents():
    # Searcher Agent
    searcher = Agent(
        role='Research Searcher',
        goal='Find comprehensive and relevant information about the given topic',
        backstory='You are an expert researcher with access to web search capabilities. You excel at finding accurate and up-to-date information from various sources.',
        tools=[WebSearchTool()],
        verbose=True,
        allow_delegation=False,
        llm=model if model else None
    )
    
    # Summarizer Agent
    summarizer = Agent(
        role='Information Summarizer',
        goal='Condense research findings into clear, organized bullet points',
        backstory='You are a skilled technical writer who specializes in distilling complex information into digestible summaries. You maintain accuracy while improving readability.',
        verbose=True,
        allow_delegation=False,
        llm=model if model else None
    )
    
    # Verifier Agent
    verifier = Agent(
        role='Fact Checker and Report Formatter',
        goal='Verify information accuracy and format it into a professional research report',
        backstory='You are a meticulous fact-checker and report formatter. You ensure all information is accurate, well-organized, and professionally presented.',
        verbose=True,
        allow_delegation=False,
        llm=model if model else None
    )
    
    return searcher, summarizer, verifier

def create_tasks(query: str, searcher: Agent, summarizer: Agent, verifier: Agent):
    # Task 1: Search for information
    search_task = Task(
        description=f"""
        Search for comprehensive information about: {query}
        
        Use the web search tool to find relevant, accurate, and up-to-date information.
        Focus on finding multiple perspectives and credible sources.
        Return detailed findings that can be used for further processing.
        """,
        agent=searcher,
        expected_output="Detailed search results with comprehensive information about the topic"
    )
    
    # Task 2: Summarize findings
    summarize_task = Task(
        description=f"""
        Summarize the research findings about: {query}
        
        Take the search results and condense them into clear, organized bullet points.
        Maintain accuracy while improving readability.
        Structure the information logically with key points highlighted.
        """,
        agent=summarizer,
        expected_output="Well-organized summary with bullet points covering the main aspects of the topic"
    )
    
    # Task 3: Verify and format report
    verify_task = Task(
        description=f"""
        Create a final research report about: {query}
        
        Review the summarized information for accuracy and completeness.
        Format it into a professional research report with:
        - Executive summary
        - Key findings
        - Detailed analysis
        - Conclusion
        
        Ensure all information is factually correct and well-presented.
        """,
        agent=verifier,
        expected_output="Professional research report with executive summary, key findings, detailed analysis, and conclusion"
    )
    
    return search_task, summarize_task, verify_task

@app.post("/research", response_model=ResearchResponse)
async def conduct_research(request: ResearchRequest):
    try:
        # Demo mode - return mock response if no API key
        if model is None:
            demo_report = f"""
# Research Report: {request.query}

## Executive Summary
This is a demo response. To get real AI-powered research, please set your GEMINI_API_KEY in the .env file.

## Key Findings
• This is a demonstration of the AI Research Assistant
• The system uses CrewAI with multiple specialized agents
• Each agent has a specific role in the research process

## Detailed Analysis
The AI Research Assistant consists of three main components:
1. **Searcher Agent**: Finds relevant information using web search
2. **Summarizer Agent**: Condenses findings into organized bullet points  
3. **Verifier Agent**: Fact-checks and formats professional reports

## Conclusion
This demo shows the system architecture. With a valid Gemini API key, the agents would work together to provide comprehensive research on any topic.

## Next Steps
1. Get a Gemini API key from: https://makersuite.google.com/app/apikey
2. Create a .env file with: GEMINI_API_KEY=your_actual_key_here
3. Restart the application for full functionality
"""
            return ResearchResponse(
                query=request.query,
                report=demo_report,
                timestamp=datetime.now().isoformat(),
                sources=["Demo Mode", "Mock Analysis"]
            )
        
        # Create agents and tasks
        searcher, summarizer, verifier = create_agents()
        search_task, summarize_task, verify_task = create_tasks(
            request.query, searcher, summarizer, verifier
        )
        
        # Create and run the crew
        crew = Crew(
            agents=[searcher, summarizer, verifier],
            tasks=[search_task, summarize_task, verify_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Execute the research process
        result = crew.kickoff()
        
        # Prepare response
        response = ResearchResponse(
            query=request.query,
            report=str(result),
            timestamp=datetime.now().isoformat(),
            sources=["Web Search", "AI Analysis"]  # Mock sources
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Research failed: {str(e)}")

@app.get("/")
async def root():
    return {"message": "AI Research Assistant API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)