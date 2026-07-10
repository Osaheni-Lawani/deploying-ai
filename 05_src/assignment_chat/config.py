import os
from dotenv import load_dotenv

load_dotenv(".secrets")

APP_NAME = "Athena AI Research Assistant"

MAX_HISTORY = 10

WEATHER_API_KEY = ""

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")

API_GATEWAY_KEY = os.getenv("API_GATEWAY_KEY")
