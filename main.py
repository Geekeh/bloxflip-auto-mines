from time import sleep
import bloxflip
import discord
import random
from discord import app_commands 

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync() 
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name = 'auto_mines', description='auto player mines') 
async def self(interaction: discord.Interaction, bet_amount : int, mine_amount : int, auth_token : str):
    if bet_amount < 5:
        await interaction.response.send_message("bet amount must be higher than 5!")
        return 0
    try:
        start_game = bloxflip.Mines.Create(betamount=bet_amount, mines=mine_amount, auth=auth_token)
        if start_game.status_code == 400:
            await interaction.response.send_message("Failed to start game | Bet amount prob higher than balance")
            return 0
        bloxflip.Currency.balance(auth=auth_token)
    except:
        await interaction.response.send_message("invalid auth token")
        return 0
    times = range(mine_amount)

    mines = bloxflip.Mines(auth)

    await interaction.response.send_message('Attempting to click mines')
    try:
        for x in times:
            try:
                a = random.randint(0, 24)
                mines.choose(a)
            except:
                balance = Currency.balance(auth=auth_token)
                emved = discord.Embed(color=0xff0000)
                emved.add_field(name='AUTOMATED MINES', value=f'You Lost! | Balance: **{balance}**')
                emved.set_footer(text='MADE BY Geek#2526, MODIFIED BY static#4444')
                await interaction.followup.send(embed=emved)
                return
        
    except:
        await interaction.followup.send("failed to click mines")
        return 0

    try:
        mines.cashout()
        balance = Currency.balance(auth=auth_token)
        em = discord.Embed(color=0x00ff00)
        em.add_field(name='AUTOMATED MINES', value=f'You Won! | Balance: **{balance}**')
        em.set_footer(text='MADE BY Geek#2526, MODIFIED BY static#4444')
        await interaction.followup.send(embed=em)
    except:
        balance = Currency.balance(auth=auth_token)
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name='AUTOMATED MINES', value=f'You Lost! | Balance: **{balance}**')
        em.set_footer(text='MADE BY Geek#2526, MODIFIED BYstatic#4444')
        await interaction.followup.send(embed=embed)

client.run('bot token here')
