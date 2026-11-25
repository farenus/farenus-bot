import discord
import discord.app_commands
import discord.ext.commands
import httpx

from farenus_bot import bot


class Minecraft(discord.ext.commands.Cog):
    def __init__(self, bot: bot.Bot):
        self.bot = bot

    @discord.app_commands.command(
        name="wl", description="dodaj użytkownika na serwer minecraft"
    )
    @discord.app_commands.describe(player="wprowadź nick gracza")
    async def wl_command(self, interaction: discord.Interaction, player: str):
        await interaction.response.defer(ephemeral=True)
        try:
            response = await self.bot.api.post(
                "/minecraft/whitelist/add", json={"player": player}
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            print(e)
            await interaction.followup.send("serwer API odpowiedział błędem")
            return
        except httpx.RequestError as e:
            print(e)
            await interaction.followup.send("serwer API nie odpowiada")
            return
        try:
            await interaction.user.edit(nick=player)
        except discord.Forbidden as e:
            print(e)
            await interaction.followup.send(
                f"dodano gracza **{player}** na serwer minecraft, ale nie udało się zmienić nazwy użytkownika"
            )
            return
        await interaction.followup.send(
            f"dodano gracza **{player}** na serwer minecraft"
        )


async def setup(bot):
    await bot.add_cog(Minecraft(bot))
