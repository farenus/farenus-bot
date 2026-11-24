import discord
import discord.ext.commands

from farenus_bot import config


class Bot(discord.ext.commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        guild = discord.Object(id=int(config.DEV_GUILD_ID))

        @self.tree.command(name="ping", description="sprawdź, czy bot odpowiada")
        async def ping_command(interaction):
            await interaction.response.send_message("pong")

        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

    async def on_ready(self):
        print(f"zalogowano jako {self.user}")
