# Multi-Agent Tourism System Architecture

## Overview

This document describes the architecture of the Multi-Agent Tourism System, which follows a hierarchical agent-based design pattern.

## Agent Hierarchy

```
Tourism Agent (Parent)
├── Weather Agent (Child)
├── Places Agent (Child)
└── Geocoding Service (Utility)
```

## Component Details

### Tourism Agent (Parent Agent)
- **File**: `agents/tourism_agent.py`
- **Role**: Orchestrates the entire system
- **Responsibilities**:
  - Parse user input and extract place names
  - Analyze user intent (weather, places, or both)
  - Coordinate with child agents
  - Combine and format responses

### Weather Agent (Child Agent)
- **File**: `agents/weather_agent.py`
- **Role**: Provides weather information
- **API**: Open-Meteo API
- **Data Provided**:
  - Current temperature
  - Precipitation probability

### Places Agent (Child Agent)
- **File**: `agents/places_agent.py`
- **Role**: Suggests tourist attractions
- **API**: Overpass API (OpenStreetMap data)
- **Data Provided**:
  - Up to 5 tourist attractions
  - Filters: tourism attractions, museums, parks, historic sites

### Geocoding Service (Utility Service)
- **File**: `agents/geocoding_service.py`
- **Role**: Convert place names to coordinates
- **API**: Nominatim API
- **Shared By**: Both Weather and Places agents

## Data Flow

1. User provides natural language input
2. Tourism Agent extracts place name using regex patterns
3. Tourism Agent analyzes intent (weather/places/both)
4. Tourism Agent requests data from appropriate child agents
5. Child agents use Geocoding Service to get coordinates
6. Child agents fetch data from respective APIs
7. Tourism Agent combines responses and returns to user

## API Integration

### Open-Meteo API
- **Endpoint**: `https://api.open-meteo.com/v1/forecast`
- **Parameters**: latitude, longitude, current weather variables
- **Rate Limiting**: None specified, but we implement respectful usage

### Overpass API
- **Endpoint**: `https://overpass-api.de/api/interpreter`
- **Query Language**: Overpass QL
- **Search Criteria**: Tourism attractions, museums, parks, historic sites within 20km radius

### Nominatim API
- **Endpoint**: `https://nominatim.openstreetmap.org/search`
- **Rate Limiting**: 1 second delay between requests
- **User Agent**: Required for API access

## Error Handling

1. **Invalid Place Names**: Geocoding service returns None, agents respond with "place doesn't exist" message
2. **API Failures**: Network errors caught and reported to user
3. **Empty Results**: Graceful fallback messages when no attractions found
4. **Timeouts**: All API calls have 10-30 second timeouts

## Natural Language Processing

The system uses regex patterns to extract place names from conversational input:

- `"going to X"` → extracts X
- `"visit X"` → extracts X
- `"trip to X"` → extracts X
- `"in X"` → extracts X

Intent analysis looks for keywords:
- Weather: temperature, weather, rain, climate
- Places: places, attractions, plan, trip, visit

## Extensibility

The architecture is designed for easy extension:

1. **New Agents**: Add new child agents by implementing similar API integration patterns
2. **New APIs**: Replace or add alternative API services in existing agents
3. **Enhanced NLP**: Improve place name extraction and intent analysis
4. **Caching**: Add response caching to reduce API calls
5. **Personalization**: Add user preferences and history