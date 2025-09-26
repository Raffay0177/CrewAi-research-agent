#!/usr/bin/env python3
"""
CLI Interface for AI Research Assistant
"""

import requests
import json
import time
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ResearchAssistantCLI:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.history = []
        
    def display_banner(self):
        """Display the application banner"""
        print("=" * 60)
        print("🤖 AI Research Assistant CLI")
        print("=" * 60)
        print("Powered by CrewAI + Gemini API")
        print("=" * 60)
        print()
        
    def display_menu(self):
        """Display the main menu"""
        print("\n📋 Menu Options:")
        print("1. 🔍 Conduct Research")
        print("2. 📚 View Research History")
        print("3. ❌ Exit")
        print()
        
    def check_api_connection(self):
        """Check if the API is running"""
        try:
            response = requests.get(f"{self.base_url}/health", timeout=5)
            if response.status_code == 200:
                print("✅ API connection successful!")
                return True
        except requests.exceptions.RequestException:
            print("❌ Cannot connect to API. Make sure the backend is running on http://localhost:8000")
            return False
        return False
        
    def conduct_research(self):
        """Conduct research on a given topic"""
        print("\n🔍 Research Mode")
        print("-" * 30)
        
        query = input("Enter your research topic: ").strip()
        if not query:
            print("❌ Please enter a valid research topic.")
            return
            
        print(f"\n🚀 Starting research on: '{query}'")
        print("⏳ This may take a few moments...")
        
        try:
            # Make API request
            response = requests.post(
                f"{self.base_url}/research",
                json={"query": query},
                timeout=60
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Display results
                self.display_research_results(data)
                
                # Add to history
                self.history.append({
                    "query": data["query"],
                    "timestamp": data["timestamp"],
                    "report_preview": data["report"][:200] + "..." if len(data["report"]) > 200 else data["report"]
                })
                
            else:
                print(f"❌ Research failed: {response.status_code}")
                print(f"Error: {response.text}")
                
        except requests.exceptions.Timeout:
            print("⏰ Request timed out. The research might be taking longer than expected.")
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error: {e}")
            
    def display_research_results(self, data):
        """Display research results in a formatted way"""
        print("\n" + "=" * 60)
        print("📊 RESEARCH RESULTS")
        print("=" * 60)
        print(f"🔍 Query: {data['query']}")
        print(f"⏰ Timestamp: {data['timestamp']}")
        print(f"📚 Sources: {', '.join(data['sources'])}")
        print("\n📋 Report:")
        print("-" * 40)
        print(data['report'])
        print("=" * 60)
        
    def view_history(self):
        """Display research history"""
        if not self.history:
            print("\n📚 No research history found.")
            return
            
        print("\n📚 Research History")
        print("=" * 50)
        
        for i, entry in enumerate(self.history, 1):
            print(f"\n{i}. 🔍 Query: {entry['query']}")
            print(f"   ⏰ Time: {entry['timestamp']}")
            print(f"   📄 Preview: {entry['report_preview']}")
            print("-" * 50)
            
    def run(self):
        """Main application loop"""
        self.display_banner()
        
        # Check API connection
        if not self.check_api_connection():
            print("\n💡 To start the backend server, run:")
            print("   cd backend && python main.py")
            print("\n   Or use Docker:")
            print("   docker-compose up")
            return
            
        while True:
            self.display_menu()
            
            try:
                choice = input("Select an option (1-3): ").strip()
                
                if choice == "1":
                    self.conduct_research()
                elif choice == "2":
                    self.view_history()
                elif choice == "3":
                    print("\n👋 Thank you for using AI Research Assistant!")
                    break
                else:
                    print("❌ Invalid choice. Please select 1, 2, or 3.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ An error occurred: {e}")

def main():
    """Main entry point"""
    cli = ResearchAssistantCLI()
    cli.run()

if __name__ == "__main__":
    main()
