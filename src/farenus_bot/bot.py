import discord
import discord.ext.commands

intents = discord.Intents.default()

bot = discord.ext.commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"zalogowano jako {bot.user}")
