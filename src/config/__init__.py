# config.py
from dotenv import load_dotenv
import os

load_dotenv()

FREESOUND_API_KEY = os.getenv("FREESOUND_API_KEY")
FREESOUND_CLIENT_ID = os.getenv("FREESOUND_CLIENT_ID")
