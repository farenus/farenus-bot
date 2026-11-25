import logging

import discord
import discord.app_commands
import discord.ext.commands
import httpx

from farenus_bot import bot
from farenus_bot import config

logger = logging.getLogger(__name__)


class Minecraft(discord.ext.commands.Cog):
    def __init__(self, bot: bot.Bot):
        self.bot = bot

    @discord.app_commands.command(
        name="wl", description="dodaj użytkownika na serwer minecraft"
    )
    @discord.app_commands.describe(player="wprowadź nick gracza")
    async def wl_command(self, interaction: discord.Interaction, player: str):
        await interaction.response.defer(ephemeral=True)
        logger.info(
            "/wl user=%s id=%s player=%s",
            interaction.user,
            interaction.user.id,
            player,
        )

        if interaction.guild is None:
            await interaction.followup.send("ta komenda działa tylko na serwerze")
            return

        role = interaction.guild.get_role(int(config.WHITELIST_ROLE_ID))
        if role is None:
            logger.error("nie znaleziono roli id=%s", config.WHITELIST_ROLE_ID)
            await interaction.followup.send(
                "rola whitelist nie istnieje, skontaktuj się z administratorem"
            )
            return

        try:
            response = await self.bot.api.post(
                "/minecraft/whitelist/add", json={"player": player}
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            logger.warning(
                "API odrzuciło player=%s status=%s", player, e.response.status_code
            )
            await interaction.followup.send("serwer API odpowiedział błędem")
            return
        except httpx.RequestError as e:
            logger.error("API nie odpowiada: %s", e)
            await interaction.followup.send("serwer API nie odpowiada")
            return

        try:
            await interaction.user.add_roles(role)
        except discord.Forbidden:
            logger.warning("brak uprawnień do roli user=%s", interaction.user)
            await interaction.followup.send(
                f"dodano gracza **{player}** na serwer minecraft, "
                "ale nie udało się nadać roli"
            )
            return

        try:
            await interaction.user.edit(nick=player)
        except discord.Forbidden:
            logger.warning("brak uprawnień do nicku user=%s", interaction.user)
            await interaction.followup.send(
                f"dodano gracza **{player}** na serwer minecraft i nadano rolę, "
                "ale nie udało się zmienić nicku"
            )
            return

        logger.info("/wl OK user=%s player=%s", interaction.user, player)
        await interaction.followup.send(
            f"dodano gracza **{player}** na serwer minecraft"
        )


async def setup(bot):
    await bot.add_cog(Minecraft(bot))
