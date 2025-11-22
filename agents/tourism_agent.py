"""
Tourism Agent - Parent agent that orchestrates the weather and places agents.
"""

import re
from .weather_agent import WeatherAgent
from .places_agent import PlacesAgent

class TourismAgent:
    """Parent agent that orchestrates the tourism system."""
    
    def __init__(self):
        self.weather_agent = WeatherAgent()
        self.places_agent = PlacesAgent()
    
    def extract_place_name(self, user_input: str) -> str:
        """
        Extract place name from user input.
        
        Args:
            user_input: User's input text
            
        Returns:
            Extracted place name
        """
        # Look for patterns like "going to X" or "go to X"
        patterns = [
            r"going?\s+to\s+go\s+to\s+([^,?.!]+)",  # Handle "going to go to X"
            r"going?\s+to\s+([^,?.!]+)",
            r"visit\s+([^,?.!]+)",
            r"trip\s+to\s+([^,?.!]+)",
            r"in\s+([^,?.!]+)",
        ]
        
        for pattern in patterns:
            match = re.search(pattern, user_input, re.IGNORECASE)
            if match:
                place = match.group(1).strip()
                # Remove common words that might be captured
                place = re.sub(r'\b(let\'s|plan|my|trip|what|is|the|temperature|there|and|are|places|can|i)\b', '', place, flags=re.IGNORECASE)
                # Clean up extra commas and spaces
                place = re.sub(r'[,\s]+$', '', place)
                return place.strip()
        
        # If no pattern matches, try to find a capitalized word (likely a place name)
        words = user_input.split()
        for word in words:
            if word[0].isupper() and len(word) > 2 and word not in ['I\'m', 'And', 'What']:
                return word
        
        return ""
    
    def analyze_intent(self, user_input: str) -> dict:
        """
        Analyze user intent to determine what information they want.
        
        Args:
            user_input: User's input text
            
        Returns:
            Dictionary with intent analysis
        """
        user_input_lower = user_input.lower()
        
        # Check for weather-related keywords
        weather_keywords = ['weather', 'temperature', 'temp', 'rain', 'sunny', 'climate']
        wants_weather = any(keyword in user_input_lower for keyword in weather_keywords)
        
        # Check for places-related keywords  
        places_keywords = ['places', 'attractions', 'tourist', 'sights', 'plan my trip']
        wants_places = any(keyword in user_input_lower for keyword in places_keywords)
        
        # Special handling for "visit" - check context
        if 'visit' in user_input_lower and 'places' in user_input_lower:
            wants_places = True
        elif 'visit' in user_input_lower and not wants_weather:
            wants_places = True
            
        # Special handling for "plan" - only if it's "plan my trip" or similar
        if 'plan' in user_input_lower and 'trip' in user_input_lower:
            wants_places = True
        
        # If only weather is mentioned, don't default to places
        if wants_weather and not wants_places:
            return {
                'wants_weather': True,
                'wants_places': False
            }
        
        # If neither is explicitly mentioned, default to places for trip planning
        if not wants_weather and not wants_places:
            wants_places = True
        
        return {
            'wants_weather': wants_weather,
            'wants_places': wants_places
        }
    
    def process_request(self, user_input: str) -> str:
        """
        Process user request and coordinate with child agents.
        
        Args:
            user_input: User's input text
            
        Returns:
            Response from the tourism system
        """
        place_name = self.extract_place_name(user_input)
        
        if not place_name:
            return "I couldn't identify a place name in your request. Please mention a specific location you'd like to visit."
        
        intent = self.analyze_intent(user_input)
        
        responses = []
        
        # Get weather information if requested
        if intent['wants_weather']:
            weather_response = self.weather_agent.get_weather(place_name)
            responses.append(weather_response)
        
        # Get places information if requested
        if intent['wants_places']:
            places_response = self.places_agent.get_tourist_attractions(place_name)
            responses.append(places_response)
        
        # If neither weather nor places are explicitly requested, default to places
        if not intent['wants_weather'] and not intent['wants_places']:
            places_response = self.places_agent.get_tourist_attractions(place_name)
            responses.append(places_response)
        
        # Combine responses
        if len(responses) == 1:
            return responses[0]
        else:
            # Both weather and places requested
            weather_part = responses[0]
            places_part = responses[1]
            
            # Extract just the weather info and places list
            if "it's currently" in weather_part:
                weather_info = weather_part.split("it's currently")[1]
                places_info = places_part.split("these are the places you can go,\n")[1] if "these are the places you can go,\n" in places_part else places_part
                
                return f"In {place_name} it's currently{weather_info} And these are the places you can go:\n{places_info}"
            else:
                return " ".join(responses)