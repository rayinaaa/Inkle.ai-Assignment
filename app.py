#!/usr/bin/env python3
"""
Flask web application for the Multi-Agent Tourism System
"""

from flask import Flask, render_template, request, jsonify
from agents.tourism_agent import TourismAgent
import threading
import time

app = Flask(__name__)
tourism_agent = TourismAgent()

@app.route('/')
def home():
    """Main page with the chat interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint for processing chat messages"""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        # Process the request with the tourism agent
        response = tourism_agent.process_request(user_message)
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': f'Error processing request: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/api/examples')
def get_examples():
    """Get example queries"""
    examples = [
        "What's the weather in Paris?",
        "I want to visit London, show me places to go",
        "I'm going to Tokyo, what's the temperature and places to visit?",
        "Tourist attractions in Rome",
        "Weather in New York",
        "I'm planning to visit Dubai, what should I expect?"
    ]
    return jsonify({'examples': examples})

if __name__ == '__main__':
    print("🌍 Starting Tourism Planning Assistant Web Interface...")
    print("🚀 Access the application at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)