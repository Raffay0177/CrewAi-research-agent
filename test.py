#!/usr/bin/env python3
"""
Test script for AI Research Assistant
"""

import requests
import json
import time
import os
from dotenv import load_dotenv

def test_api_connection():
    """Test if the API is running"""
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print("✅ API connection successful!")
            return True
    except requests.exceptions.RequestException:
        print("❌ Cannot connect to API")
        return False
    return False

def test_research_endpoint():
    """Test the research endpoint"""
    test_queries = [
        "artificial intelligence",
        "climate change",
        "quantum computing"
    ]
    
    for query in test_queries:
        print(f"\n🔍 Testing research query: '{query}'")
        try:
            response = requests.post(
                "http://localhost:8000/research",
                json={"query": query},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Research completed successfully!")
                print(f"📊 Report length: {len(data['report'])} characters")
                print(f"📚 Sources: {', '.join(data['sources'])}")
            else:
                print(f"❌ Research failed: {response.status_code}")
                print(f"Error: {response.text}")
                
        except requests.exceptions.Timeout:
            print("⏰ Request timed out")
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error: {e}")

def main():
    """Main test function"""
    print("🧪 AI Research Assistant Test Suite")
    print("=" * 40)
    
    # Load environment variables
    load_dotenv()
    
    # Check API key
    if not os.getenv("GEMINI_API_KEY"):
        print("⚠️  GEMINI_API_KEY not found in environment variables")
        print("   Please add your API key to .env file")
        return
    
    # Test API connection
    if not test_api_connection():
        print("\n💡 To start the backend server, run:")
        print("   cd backend && python main.py")
        return
    
    # Test research endpoint
    test_research_endpoint()
    
    print("\n🎉 Test suite completed!")

if __name__ == "__main__":
    main()
