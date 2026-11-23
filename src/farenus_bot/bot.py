import discord
import discord.ext.commands


class Bot(discord.ext.commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f"zalogowano jako {self.user}")
