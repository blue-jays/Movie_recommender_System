"""
Frontend Configuration
Centralized config for Gradio UI.

"""
import os
from dotenv import load_dotenv

load_dotenv()    # to load the env


# API configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000" )

# TMDB configuration
TMDB_API_KEY = os.getenv("TMDB_API_KEY", " ")
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


# Gradio Configs
GRADIO_HOST = os.getenv("GRADIO_HOST", "0.0.0.0")
GRADIO_PORT = int(os.getenv("GRADIO_PORT", 7860))
GRADIO_SHARE = os.getenv("GRADIO_SHARE", "false").lower() == "true"

# UI CONFIGURATIOn
AVAILABLE_GENRES = [
    "Action", "Adventure", "Animation", "Children", "Comedy",
    "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir",
    "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
    "Thriller", "War", "Western"
]

NUM_GENRES_TO_SELECT = 3
MOVIES_PER_GENRE = 5
TOTAL_ONBOARDING_RATINGS = NUM_GENRES_TO_SELECT * MOVIES_PER_GENRE  # 15

# 
COLD_START_THRESHOLD = 30 