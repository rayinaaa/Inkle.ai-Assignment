"""
Weather Agent that provides current weather information using Open-Meteo API.
"""

import requests
from typing import Optional, Tuple
from .geocoding_service import GeocodingService

class WeatherAgent:
    """Agent responsible for providing weather information."""
    
    def __init__(self):
        self.api_url = "https://api.open-meteo.com/v1/forecast"
        self.geocoding = GeocodingService()
    
    def get_weather(self, place_name: str) -> str:
        """
        Get current weather for a given place.
        
        Args:
            place_name: Name of the place to get weather for
            
        Returns:
            String with weather information or error message
        """
        try:
            # First get coordinates
            coordinates = self.geocoding.get_coordinates(place_name)
            
            if not coordinates:
                return f"I don't know if this place '{place_name}' exists. Please check the spelling or try a different location."
            
            lat, lon = coordinates
            
            # Get weather data
            params = {
                'latitude': lat,
                'longitude': lon,
                'current': ['temperature_2m', 'precipitation_probability'],
                'timezone': 'auto'
            }
            
            response = requests.get(self.api_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if 'current' in data:
                current = data['current']
                temp = current.get('temperature_2m')
                precip_prob = current.get('precipitation_probability', 0)
                
                return f"In {place_name} it's currently {temp}°C with a chance of {precip_prob}% to rain."
            else:
                return f"Unable to get weather data for {place_name}."
                
        except Exception as e:
            return f"Error getting weather for {place_name}: {str(e)}"