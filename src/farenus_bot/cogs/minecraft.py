import discord
import discord.app_commands
import discord.ext.commands

from farenus_bot import bot


class Minecraft(discord.ext.commands.Cog):
    def __init__(self, bot: bot.Bot):
        self.bot = bot

    @discord.app_commands.command(
        name="wl", description="dodaj użytkownika na serwer minecraft"
    )
    @discord.app_commands.describe(player="wprowadź nick gracza")
    async def wl_command(self, interaction: discord.Interaction, player: str):
        await interaction.response.defer()
        response = await self.bot.api.post(
            "/minecraft/whitelist/add", json={"player": player}
        )
        response.raise_for_status()
        await interaction.followup.send(
            f"dodano gracza **{player}** na serwer minecraft"
        )
        print(self.bot.api.headers)


async def setup(bot):
    await bot.add_cog(Minecraft(bot))
