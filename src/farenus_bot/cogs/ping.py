import discord
import discord.app_commands
import discord.ext.commands


class Ping(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="ping", description="sprawdź, czy bot odpowiada")
    async def ping_command(self, interaction: discord.Interaction):
        await interaction.response.send_message("pong")


async def setup(bot):
    await bot.add_cog(Ping(bot))
