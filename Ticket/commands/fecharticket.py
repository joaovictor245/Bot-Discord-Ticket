import discord
import random
from discord import app_commands
from discord.ext import commands

id_cargo_atendente = 12345678910 #Coloca o id do cargo aqui

class Fecharticket(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="fecharticket",description='Feche um atendimento atual.')
    async def _fecharticket(self ,interaction: discord.Interaction):
        mod = interaction.guild.get_role(id_cargo_atendente)
        if str(interaction.user.id) in interaction.channel.name or mod in interaction.author.roles:
            await interaction.response.send_message(f"O ticket foi arquivado por {interaction.user.mention}, obrigado por entrar em contato!")
            await interaction.channel.edit(archived=True,locked=True)
        else:
            await interaction.response.send_message("Isso não pode ser feito aqui...")


async def setup(client):
    await client.add_cog(Fecharticket(client))
