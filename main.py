#!/usr/bin/env python3
"""
Multi-Agent Tourism System
Main entry point for the tourism planning system.
"""

from agents.tourism_agent import TourismAgent

def main():
    """Main function to run the tourism system."""
    print("🌍 Welcome to the Multi-Agent Tourism System!")
    print("Ask me about weather, places to visit, or both!")
    print("Type 'quit' to exit.\n")
    
    tourism_agent = TourismAgent()
    
    while True:
        try:
            user_input = input("User: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Thank you for using the Tourism System! Safe travels! 🧳")
                break
            
            if not user_input:
                continue
            
            response = tourism_agent.process_request(user_input)
            print(f"Tourism Agent: {response}\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()