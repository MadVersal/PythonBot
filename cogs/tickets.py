from discord.ext import commands
import discord
from datetime import datetime

class CreateTicketButton(discord.ui.Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.primary, label="Crear Ticket", custom_id="create_ticket")
    
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(CreateTicketModal())

class CreateTicketModal(discord.ui.Modal, title="Crear Ticket"):
    reason = discord.ui.TextInput(
        label="¿Cuál es el motivo de tu ticket?",
        placeholder="Escribe el motivo aquí",
        style=discord.TextStyle.paragraph,
        required=True,
        max_length=1000
    )

    async def on_submit(self, interaction: discord.Interaction):
        # Obtener el cog de tickets
        tickets_cog = interaction.client.get_cog("Tickets")
        if tickets_cog:
            await tickets_cog.create_ticket(interaction, str(self.reason))

class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(CreateTicketButton())

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ticket_counter = 0
        self.support_category_name = "Tickets"

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_tickets(self, ctx):
        """Configura la categoría para los tickets"""
        category = discord.utils.get(ctx.guild.categories, name=self.support_category_name)
        if not category:
            category = await ctx.guild.create_category(self.support_category_name)
            await ctx.send("Sistema de tickets configurado correctamente.")
        else:
            await ctx.send("El sistema de tickets ya está configurado.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def panel(self, ctx):
        """Crea el panel de tickets con botón"""
        embed = discord.Embed(
            title="Sistema de Tickets",
            description="¿Necesitas ayuda? ¡Crea un ticket haciendo clic en el botón de abajo!\n\n"
                      "**¿Cuándo crear un ticket?**\n"
                      "• Si tienes alguna duda o problema\n"
                      "• Para reportar a un usuario\n"
                      "• Para contactar al staff\n\n"
                      "Por favor, sé paciente y espera a que un miembro del staff te atienda.",
            color=discord.Color.blue()
        )
        embed.set_footer(text="Sistema de Tickets • @MadVersal 2025")
        
        view = TicketView()
        await ctx.send(embed=embed, view=view)

    async def create_ticket(self, interaction: discord.Interaction, reason: str):
        """Crea un nuevo ticket de soporte"""
        category = discord.utils.get(interaction.guild.categories, name=self.support_category_name)
        if not category:
            return await interaction.response.send_message(
                "El sistema de tickets no está configurado. Un administrador debe usar !setup_tickets primero.",
                ephemeral=True
            )

        self.ticket_counter += 1
        channel_name = f"ticket-{interaction.user.name}-{self.ticket_counter}"
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            interaction.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        
        staff_roles = [role for role in interaction.guild.roles if any(keyword in role.name.lower() for keyword in ['staff', 'admin', 'mod'])]
        for role in staff_roles:
            overwrites[role] = discord.PermissionOverwrite(read_messages=True, send_messages=True)
        
        ticket_channel = await interaction.guild.create_text_channel(
            channel_name,
            category=category,
            overwrites=overwrites
        )

        embed = discord.Embed(title="Nuevo Ticket", color=discord.Color.blue())
        embed.add_field(name="Creador", value=interaction.user.mention, inline=False)
        embed.add_field(name="Razón", value=reason, inline=False)
        embed.add_field(name="ID del Ticket", value=f"#{self.ticket_counter}", inline=False)
        embed.add_field(name="Fecha", value=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.set_footer(text="Usa !close para cerrar el ticket")

        class CloseButton(discord.ui.Button):
            def __init__(self):
                super().__init__(style=discord.ButtonStyle.danger, label="Cerrar Ticket", custom_id="close_ticket")

            async def callback(self, button_interaction: discord.Interaction):
                if not (button_interaction.user.guild_permissions.administrator or 
                        button_interaction.user == interaction.user or
                        any(role.name.lower() in ['staff', 'admin', 'mod'] for role in button_interaction.user.roles)):
                    await button_interaction.response.send_message("No tienes permiso para cerrar este ticket.", ephemeral=True)
                    return

                await button_interaction.response.send_message("Cerrando ticket en 5 segundos...")
                await discord.utils.sleep_until(datetime.now().timestamp() + 5)
                await ticket_channel.delete()

        view = discord.ui.View(timeout=None)
        view.add_item(CloseButton())
        await ticket_channel.send(embed=embed, view=view)
        await ticket_channel.send(f"{interaction.user.mention} Bienvenido a tu ticket. Un staff te atenderá pronto.")
        await interaction.response.send_message(f"✅ Tu ticket ha sido creado en {ticket_channel.mention}", ephemeral=True)

    @commands.command()
    async def close(self, ctx):
        """Cierra un ticket"""
        if not ctx.channel.name.startswith("ticket-"):
            return await ctx.send("❌ Este comando solo puede usarse en canales de ticket.")
        
        if not (ctx.author.guild_permissions.administrator or ctx.channel.permissions_for(ctx.author).read_messages):
            return await ctx.send("❌ No tienes permiso para cerrar este ticket.")

        await ctx.send("Cerrando ticket en 5 segundos...")
        await discord.utils.sleep_until(datetime.now().timestamp() + 5)
        await ctx.channel.delete()

async def setup(bot):
    cog = Tickets(bot)
    await bot.add_cog(cog)
    print("[DEBUG] Cog Tickets cargado y comandos de tickets registrados.")
