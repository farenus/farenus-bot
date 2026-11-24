import discord
import discord.ext.commands
import httpx

from farenus_bot import config


class Bot(discord.ext.commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        self.api = httpx.AsyncClient(
            base_url=config.API_BASE_URL,
            headers={config.API_KEY_HEADER: config.API_KEY},
            timeout=10,
        )
        await self.load_extension("farenus_bot.cogs.ping")
        guild = discord.Object(id=int(config.DEV_GUILD_ID))
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

    async def close(self):
        await self.api.aclose()
        await super().close()

    async def on_ready(self):
        print(f"zalogowano jako {self.user}")
