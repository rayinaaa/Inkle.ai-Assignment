# Multi-Agent Tourism System

A Python-based multi-agent system that helps users plan their trips by providing weather information and tourist attraction suggestions for any location worldwide.

## System Architecture

The system implements a hierarchical multi-agent architecture:

- **Parent Agent**: Tourism AI Agent (orchestrates the entire system)
- **Child Agent 1**: Weather Agent (provides current weather using Open-Meteo API)
- **Child Agent 2**: Places Agent (suggests up to 5 tourist attractions using Overpass API)
- **Supporting Service**: Geocoding Service (converts place names to coordinates using Nominatim API)

## Features

✅ **Weather Information**: Get current temperature and precipitation probability  
✅ **Tourist Attractions**: Discover up to 5 popular places to visit  
✅ **Smart Intent Analysis**: Automatically determines what information the user wants  
✅ **Error Handling**: Graceful handling of non-existent or misspelled place names  
✅ **Natural Language Processing**: Extracts place names from conversational input  
✅ **Real-time Data**: Uses live APIs for accurate, up-to-date information  

## APIs Used

- **Weather**: [Open-Meteo API](https://api.open-meteo.com/v1/forecast) - Free weather forecast API
- **Places**: [Overpass API](https://overpass-api.de/api/interpreter) - OpenStreetMap data for tourist attractions
- **Geocoding**: [Nominatim API](https://nominatim.openstreetmap.org/search) - Place name to coordinates conversion

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode
```bash
python main.py
```

### Run Examples
```bash
python examples.py
```

### Run Tests
```bash
python test_system.py
```

## Example Interactions

### Example 1: Trip Planning
**Input**: "I'm going to go to Bangalore, let's plan my trip."  
**Output**: 
```
In Bangalore these are the places you can go,
Lalbagh
Sri Chamarajendra Park
Bangalore palace
Bannerghatta National Park
Jawaharlal Nehru Planetarium
```

### Example 2: Weather Query
**Input**: "I'm going to go to Bangalore, what is the temperature there?"  
**Output**: 
```
In Bangalore it's currently 24°C with a chance of 35% to rain.
```

### Example 3: Combined Query
**Input**: "I'm going to go to Bangalore, what is the temperature there? And what are the places I can visit?"  
**Output**: 
```
In Bangalore it's currently 24°C with a chance of 35% to rain. And these are the places you can go:
Lalbagh
Sri Chamarajendra Park
Bangalore palace
Bannerghatta National Park
Jawaharlal Nehru Planetarium
```

### Example 4: Error Handling
**Input**: "I'm going to go to NonExistentCity, let's plan my trip."  
**Output**: 
```
I don't know if this place 'NonExistentCity' exists. Please check the spelling or try a different location.
```

## Project Structure

```
├── agents/
│   ├── __init__.py
│   ├── tourism_agent.py      # Parent agent (orchestrator)
│   ├── weather_agent.py      # Weather information agent
│   ├── places_agent.py       # Tourist attractions agent
│   └── geocoding_service.py  # Place name to coordinates service
├── main.py                   # Interactive main application
├── examples.py              # Example usage demonstrations
├── test_system.py           # System tests
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Technical Details

- **Language**: Python 3.6+
- **Dependencies**: Only `requests` for API calls
- **API Rate Limiting**: Implements respectful delays between API calls
- **Error Handling**: Comprehensive error handling for network issues and invalid inputs
- **Intent Recognition**: Smart natural language processing to understand user requests