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


@tree.command(name = 'mines', description='auto player mines') 
async def self(interaction: discord.Interaction, bet_amount : int, mine_amount : int, auth_token : str):
    if bet_amount < 5:
        await interaction.response.send_message("bet amount must be higher than 5!")
        return 0
    try:
        start_game = bloxflip.Mines.Create(betamount=bet_amount, mines=mine_amount, auth=auth_token)
        if start_game.status_code == 400:
            await interaction.response.send_message("Failed to start game | Bet amount prob higher than balance")
            return 0
        await interaction.response.send_message("Game started! use /choose_mine to click a mine")
    except:
        await interaction.response.send_message("Error of the following: Bet amount, Mine amount, Auth token, api did not respond")

@tree.command(name = 'choose_mine', description='choose how many mines u want to click') 
async def self(interaction: discord.Interaction, mine_amount : int, auth_token : str):
    try:
        bloxflip.Currency.Balance(auth=auth_token)
    except:
        await interaction.response.send_message("invalid auth token")
        return 0
    times = range(mine_amount)
    await interaction.response.send_message('Clicking mines...')
    try:
        for x in times:
            try:
                a = random.randint(0, 24)
                bloxflip.Mines.Choose(choice=int(a), auth=auth_token)
                await interaction.followup.send('clicked mine')
            except:
                await interaction.followup.send("failed to click mines")
                return
        
    except:
        await interaction.followup.send("failed to click mines")

@tree.command(name='cashout', description='cashout of a mines game')
async def self(interaction: discord.Interaction, auth_token : str):
    try:
        bloxflip.Currency.Balance(auth=auth_token)
    except:
        await interaction.response.send_message("invalid auth token")
        return 0
    await interaction.response.send_message("cashing out of mines game")
    try:
        bloxflip.Mines.Cashout(auth=auth_token)
        await interaction.followup.send("Cashed out of game!")
    except:
        await interaction.followup.send("not in a game")
    

client.run('bot token here')
