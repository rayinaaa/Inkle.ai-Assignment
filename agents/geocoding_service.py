"""
Geocoding service using Nominatim API to get coordinates for place names.
"""

import requests
import time
from typing import Optional, Tuple

class GeocodingService:
    """Service to get coordinates for place names using Nominatim API."""
    
    def __init__(self):
        self.base_url = "https://nominatim.openstreetmap.org/search"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'TourismAgent/1.0 (Educational Project)'
        })
    
    def get_coordinates(self, place_name: str) -> Optional[Tuple[float, float]]:
        """
        Get coordinates (latitude, longitude) for a place name.
        
        Args:
            place_name: Name of the place to geocode
            
        Returns:
            Tuple of (latitude, longitude) or None if not found
        """
        try:
            params = {
                'q': place_name,
                'format': 'json',
                'limit': 1
            }
            
            response = self.session.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            
            # Be respectful to the API
            time.sleep(1)
            
            data = response.json()
            
            if data:
                lat = float(data[0]['lat'])
                lon = float(data[0]['lon'])
                return (lat, lon)
            
            return None
            
        except Exception as e:
            print(f"Geocoding error for '{place_name}': {e}")
            return None