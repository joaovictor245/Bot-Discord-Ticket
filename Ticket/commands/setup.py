import discord
import random
from discord import app_commands
from discord.ext import commands

id_cargo_atendente = 1160350104516042885

class Dropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(value="compra",label="Compras", emoji="🛒"),
            discord.SelectOption(value="denuncia",label="Denuncias", emoji="🚨"),
            discord.SelectOption(value="atendimento",label="Atendimento", emoji="📨"),
            discord.SelectOption(value="Pagamento Freelancer",label="pagamento Freelancer", emoji="💲"),
        ]
        super().__init__(
            placeholder="Selecione uma opção...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="persistent_view:dropdown_help"
        )
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "compra":
            await interaction.response.send_message("Clique abaixo para criar um ticket", ephemeral=True, view=CreateTicket())        
        if self.values[0] == "denuncia":
            await interaction.response.send_message("Clique abaixo para criar um ticket",ephemeral=True, view=CreateTicket())
        elif self.values[0] == "atendimento":
            await interaction.response.send_message("Clique abaixo para criar um ticket ticket",ephemeral=True, view=CreateTicketcompras())
        if self.values[0] == "Pagamento Freelancer":
            await interaction.response.send_message("Clique abaixo para criar um ticket ticket",ephemeral=True, view=CreateTicketcompras())

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=40)

        self.add_item(Dropdown())

class CreateTicket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.value=None

    @discord.ui.button(label="Abrir Ticket",style=discord.ButtonStyle.blurple,emoji="➕")
    async def confirm(self,interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        self.stop()

        ticket = None
        for thread in interaction.channel.threads:
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(ephemeral=True,content=f"Você já tem um atendimento em andamento!")
                    return

        async for thread in interaction.channel.archived_threads(private=True):
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.edit_original_response(content=f"Você já tem um atendimento em andamento!",view=None)
                    return
        
        if ticket != None:
            await ticket.edit(archived=False,locked=False)
            await ticket.edit(name=f"{interaction.user.name} ({interaction.user.id})",auto_archive_duration=10080,invitable=False)
        else:
            ticket = await interaction.channel.create_thread(name=f"{interaction.user.name} ({interaction.user.id})",auto_archive_duration=10080)#,type=discord.ChannelType.public_thread)
            await ticket.edit(invitable=False)

        await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")
        await ticket.send(f"📩  **|** {interaction.user.mention} ticket criado! Envie todas as informações possíveis sobre seu caso e aguarde até que um atendente responda.\n\nApós a sua questão ser sanada, você pode usar `/fecharticket` para encerrar o atendimento!")

#compras

class CreateTicketcompras(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.value=None

    @discord.ui.button(label="Abrir Ticket discord",style=discord.ButtonStyle.blurple,emoji="➕")
    async def confirm(self,interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        self.stop()

        ticket = None
        for thread in interaction.channel.threads:
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(ephemeral=True,content=f"Você já tem um atendimento em andamento!")
                    return

        async for thread in interaction.channel.archived_threads(private=True):
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.edit_original_response(content=f"Você já tem um atendimento em andamento!",view=None)
                    return
        
        if ticket != None:
            await ticket.edit(archived=False,locked=False)
            await ticket.edit(name=f"{interaction.user.name} ({interaction.user.id})",auto_archive_duration=10080,invitable=False)
        else:
            ticket = await interaction.channel.create_thread(name=f"{interaction.user.name} ({interaction.user.id})",auto_archive_duration=10080)#,type=discord.ChannelType.public_thread)
            await ticket.edit(invitable=False)

        await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")
        await ticket.send(f"📩  **|** {interaction.user.mention} ticket criado! Envie todas as informações possíveis sobre seu caso e aguarde até que um atendente responda.\n\nApós a sua questão ser sanada, você pode usar `/fecharticket` para encerrar o atendimento!")
        
class Setup(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"comandos fde teste")


    @app_commands.command(name = 'setup', description='Setup')
    @commands.has_permissions(manage_guild=True)
    async def setup(self,interaction: discord.Interaction):
        embed=discord.Embed(title="Nome do Ticket", description="Sistema de Tickets para atendimento aos jogadores.:j_arrow: Utilize o botão abaixo para iniciar um novo Ticket.Obs: Tickets sem necessidade resultará em punição", color=0xff0000)
        embed.set_image(url="")
        embed.add_field(name="", value="", inline=False)

        await interaction.response.send_message("Mensagem do painel",ephemeral=True)
        await interaction.channel.send(embed=embed,view=DropdownView())

async def setup(client):
    await client.add_cog(Setup(client))
