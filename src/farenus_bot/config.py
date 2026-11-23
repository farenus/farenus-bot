import pathlib

import dotenv

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2]

ENV_FILE = dotenv.dotenv_values(PROJECT_ROOT / ".env")

DISCORD_TOKEN = ENV_FILE.get("DISCORD_TOKEN")
