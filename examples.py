#!/usr/bin/env python3
"""
Example usage of the Multi-Agent Tourism System
Demonstrates the three example cases from the assignment.
"""

from agents.tourism_agent import TourismAgent

def run_examples():
    """Run the example scenarios from the assignment."""
    print("🌟 Multi-Agent Tourism System Examples\n")
    
    tourism_agent = TourismAgent()
    
    examples = [
        {
            "title": "Example 1: Trip Planning",
            "input": "I'm going to go to Bangalore, let's plan my trip.",
            "description": "User wants to plan a trip - should return tourist attractions"
        },
        {
            "title": "Example 2: Weather Query", 
            "input": "I'm going to go to Bangalore, what is the temperature there?",
            "description": "User wants weather information only"
        },
        {
            "title": "Example 3: Combined Query",
            "input": "I'm going to go to Bangalore, what is the temperature there? And what are the places I can visit?",
            "description": "User wants both weather and places information"
        }
    ]
    
    for example in examples:
        print(f"📍 {example['title']}")
        print(f"Description: {example['description']}")
        print(f"Input: {example['input']}")
        print("Response:")
        
        try:
            response = tourism_agent.process_request(example['input'])
            print(response)
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    run_examples()