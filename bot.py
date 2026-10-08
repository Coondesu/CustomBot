import discord

from discord import app_commands

import os

token = os.getenv("DISCORD_TOKEN")


class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


client = MyClient()

import random


@client.tree.command(
    name="ping",
    description="If she pings..."
)
@app_commands.allowed_installs(users=True, guilds=True)
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def ping(interaction: discord.Interaction):
    randomChance = random.randint(1,5)
    status = "None"
    if (randomChance <= 2):
        status = "Pong!"
    elif (randomChance == 3):
        status = "Oops.....All berries!"
    else:
        status = "Oops.. I missed..."

    await interaction.response.send_message(status)

@client.tree.command(
    name="gamble",
    description="tip: gamble it all"
)
@app_commands.allowed_installs(users=True, guilds=True)
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def gamble(interaction: discord.Interaction):
    currencyList = ["berries", "brasilian reais", "freedom moneis", "dirty cashs", "supplies of oops all berries"]
    randomPrice = random.randint(500,1500)
    randomChance = random.randint(1,10)
    randomCurrency = random.choice(currencyList)

    status = "None"
    if (randomChance == 1):
        status = f"And i tripled it! Now i have {randomPrice*3} {randomCurrency}!!!"
    else:
        status = "But i lost it all..."

    await interaction.response.send_message(f"I gambled {randomPrice} {randomCurrency}!\n{status}")



@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

client.run(token)