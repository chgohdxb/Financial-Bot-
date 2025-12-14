"""
Configuration management for Financial Bot
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
MISTRAL_MODEL = os.getenv('MISTRAL_MODEL', 'mistral-small')
MISTRAL_API_URL = "https://api.mistral.ai/v0/chat/completions"

if not MISTRAL_API_KEY:
    raise ValueError("MISTRAL_API_KEY not found in environment variables. Please set it in .env file.")
