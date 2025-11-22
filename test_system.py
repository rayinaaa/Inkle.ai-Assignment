#!/usr/bin/env python3
"""
Test script to verify the multi-agent tourism system works correctly.
"""

from agents.tourism_agent import TourismAgent

def test_examples():
    """Test the system with the provided examples."""
    print("🧪 Testing Multi-Agent Tourism System\n")
    
    tourism_agent = TourismAgent()
    
    # Test cases from the assignment
    test_cases = [
        "I'm going to go to Bangalore, let's plan my trip.",
        "I'm going to go to Bangalore, what is the temperature there?",
        "I'm going to go to Bangalore, what is the temperature there? And what are the places I can visit?",
        "I'm going to go to NonExistentCity12345, let's plan my trip.",  # Error handling test
    ]
    
    for i, test_input in enumerate(test_cases, 1):
        print(f"Test {i}:")
        print(f"Input: {test_input}")
        print("Output:")
        
        try:
            response = tourism_agent.process_request(test_input)
            print(response)
        except Exception as e:
            print(f"Error: {e}")
        
        print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    test_examples()