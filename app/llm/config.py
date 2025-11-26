from openai import OpenAI
from os import getenv, path
from dotenv import load_dotenv
from pathlib import Path

DOTENV_PATH = Path(
    path.dirname(__file__), "..", "..", ".env"
)

load_dotenv(dotenv_path=DOTENV_PATH)

API_KEY = getenv("OPENAI_API_KEY")

MODEL = "gpt-4o-mini"
CLIENT = OpenAI(api_key=API_KEY)
