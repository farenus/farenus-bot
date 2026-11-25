import discord
import discord.app_commands
import discord.ext.commands
import httpx

from farenus_bot import bot
from farenus_bot import config


class Minecraft(discord.ext.commands.Cog):
    def __init__(self, bot: bot.Bot):
        self.bot = bot

    @discord.app_commands.command(
        name="wl", description="dodaj użytkownika na serwer minecraft"
    )
    @discord.app_commands.describe(player="wprowadź nick gracza")
    async def wl_command(self, interaction: discord.Interaction, player: str):
        await interaction.response.defer(ephemeral=True)

        if interaction.guild is None:
            await interaction.followup.send("ta komenda działa tylko na serwerze")
            return

        role = interaction.guild.get_role(int(config.WHITELIST_ROLE_ID))
        if role is None:
            await interaction.followup.send(
                "rola whitelist nie istnieje, skontaktuj się z administratorem"
            )
            return
        try:
            response = await self.bot.api.post(
                "/minecraft/whitelist/add", json={"player": player}
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            print(e)
            await interaction.followup.send("serwer API odpowiedział błędem")
            return
        except httpx.RequestError as e:
            print(e)
            await interaction.followup.send("serwer API nie odpowiada")
            return
        try:
            await interaction.user.add_roles(role)
        except discord.Forbidden:
            await interaction.followup.send(
                f"dodano gracza **{player}** na serwer minecraft, "
                "ale nie udało się nadać roli"
            )
            return
        await interaction.followup.send(
            f"dodano gracza **{player}** na serwer minecraft"
        )


async def setup(bot):
    await bot.add_cog(Minecraft(bot))
