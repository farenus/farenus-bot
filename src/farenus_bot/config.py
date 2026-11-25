import pathlib

import dotenv

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2]

ENV_FILE = dotenv.dotenv_values(PROJECT_ROOT / ".env")

DISCORD_TOKEN = ENV_FILE.get("DISCORD_TOKEN")

DEV_GUILD_ID = ENV_FILE.get("DEV_GUILD_ID")

API_BASE_URL = ENV_FILE.get("API_BASE_URL")

API_KEY_HEADER = ENV_FILE.get("API_KEY_HEADER")

API_KEY = ENV_FILE.get("API_KEY")

WHITELIST_ROLE_ID = ENV_FILE.get("WHITELIST_ROLE_ID")
