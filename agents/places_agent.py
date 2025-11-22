"""
Places Agent that suggests tourist attractions using Overpass API.
"""

import requests
from typing import List
from .geocoding_service import GeocodingService

class PlacesAgent:
    """Agent responsible for suggesting tourist attractions."""
    
    def __init__(self):
        self.api_url = "https://overpass-api.de/api/interpreter"
        self.geocoding = GeocodingService()
    
    def get_tourist_attractions(self, place_name: str) -> str:
        """
        Get tourist attractions for a given place.
        
        Args:
            place_name: Name of the place to get attractions for
            
        Returns:
            String with tourist attractions or error message
        """
        try:
            # First get coordinates
            coordinates = self.geocoding.get_coordinates(place_name)
            
            if not coordinates:
                return f"I don't know if this place '{place_name}' exists. Please check the spelling or try a different location."
            
            lat, lon = coordinates
            
            # Create Overpass query for tourist attractions
            # Search within approximately 20km radius
            bbox_size = 0.18  # roughly 20km
            south = lat - bbox_size
            north = lat + bbox_size
            west = lon - bbox_size
            east = lon + bbox_size
            
            overpass_query = f"""
            [out:json][timeout:25];
            (
              node["tourism"~"attraction|museum|gallery|zoo|theme_park|viewpoint"]({south},{west},{north},{east});
              way["tourism"~"attraction|museum|gallery|zoo|theme_park|viewpoint"]({south},{west},{north},{east});
              rel["tourism"~"attraction|museum|gallery|zoo|theme_park|viewpoint"]({south},{west},{north},{east});
              node["historic"~"castle|palace|monument|ruins"]({south},{west},{north},{east});
              way["historic"~"castle|palace|monument|ruins"]({south},{west},{north},{east});
              node["leisure"~"park|garden"]({south},{west},{north},{east});
              way["leisure"~"park|garden"]({south},{west},{north},{east});
            );
            out center meta;
            """
            
            response = requests.post(
                self.api_url, 
                data=overpass_query, 
                timeout=30,
                headers={'Content-Type': 'text/plain; charset=utf-8'}
            )
            response.raise_for_status()
            
            data = response.json()
            attractions = []
            
            for element in data.get('elements', []):
                name = element.get('tags', {}).get('name')
                if name and len(name.strip()) > 0:
                    attractions.append(name.strip())
            
            # Remove duplicates and limit to 5
            unique_attractions = list(dict.fromkeys(attractions))[:5]
            
            if unique_attractions:
                places_list = '\n'.join(unique_attractions)
                return f"In {place_name} these are the places you can go,\n{places_list}"
            else:
                return f"I couldn't find specific tourist attractions for {place_name}, but it's still worth exploring!"
                
        except Exception as e:
            return f"Error getting attractions for {place_name}: {str(e)}"