import discord, pickle
from discord import app_commands
from typing import List

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

client.aq = set()
client.sq = {}
client.hangout = {}


async def sq_autocomplete(interaction, current: str) -> List[app_commands.Choice[str]]:
    choices = client.sq.keys()
    choices = [
        app_commands.Choice(name=choice, value=choice)
        for choice in choices
        if current.lower() in choice.lower()
    ][:25]
    return choices


async def h_autocomplete(interaction, current: str) -> List[app_commands.Choice[str]]:
    choices = client.hangout.keys()
    choices = [
        app_commands.Choice(name=choice, value=choice)
        for choice in choices
        if current.lower() in choice.lower()
    ][:25]
    return choices


@client.event
async def on_ready():
    with open("archon_quest.pkl", "rb") as f:
        client.aq = pickle.load(f)

    with open("story_quest.pkl", "rb") as f:
        client.sq = pickle.load(f)

    with open("hangout.pkl", "rb") as f:
        client.hangout = pickle.load(f)

    await tree.sync()
    print("Ready!")
    return


@tree.command()
async def finishaq(interaction):
    client.aq.add(interaction.user.display_name)
    with open("archon_quest.pkl", "wb") as f:
        pickle.dump(client.aq, f)
    await interaction.response.send_message("Added name to AQ list")
    return


@tree.command()
@app_commands.autocomplete(choice=sq_autocomplete)
async def finishsq(interaction, choice: str):
    if choice not in client.sq:
        await interaction.response.send_message("Invalid name")
    else:
        client.sq[choice].add(interaction.user.display_name)
        with open("story_quest.pkl", "wb") as f:
            pickle.dump(client.sq, f)
        await interaction.response.send_message("Added name to " + choice + " SQ list")
    return


@tree.command()
@app_commands.autocomplete(choice=h_autocomplete)
async def finishh(interaction, choice: str):
    if choice not in client.hangout:
        await interaction.response.send_message("Invalid name")
    else:
        client.hangout[choice].add(interaction.user.display_name)
        with open("hangout.pkl", "wb") as f:
            pickle.dump(client.hangout, f)
        await interaction.response.send_message(
            "Added name to " + choice + " Hangout list"
        )
    return


@tree.command()
async def removeaq(interaction):
    client.aq.discard(interaction.user.display_name)
    with open("archon_quest.pkl", "wb") as f:
        pickle.dump(client.aq, f)
    await interaction.response.send_message("Removed name from AQ list")
    return


@tree.command()
@app_commands.autocomplete(choice=sq_autocomplete)
async def removesq(interaction, choice: str):
    if choice not in client.sq:
        await interaction.response.send_message("Invalid name")
    else:
        client.sq[choice].discard(interaction.user.display_name)
        with open("story_quest.pkl", "wb") as f:
            pickle.dump(client.sq, f)
        await interaction.response.send_message(
            "Removed name from " + choice + " SQ list"
        )
    return


@tree.command()
@app_commands.autocomplete(choice=h_autocomplete)
async def removeh(interaction, choice: str):
    if choice not in client.hangout:
        await interaction.response.send_message("Invalid name")
    else:
        client.hangout[choice].discard(interaction.user.display_name)
        with open("hangout.pkl", "wb") as f:
            pickle.dump(client.hangout, f)
        await interaction.response.send_message(
            "Removed name from " + choice + " Hangout list"
        )
    return


@tree.command()
async def checkaq(interaction):
    if len(client.aq) == 0:
        await interaction.response.send_message("no one")
    else:
        await interaction.response.send_message(
            ", ".join(str(x) for x in list(client.aq))
        )
    return


@tree.command()
@app_commands.autocomplete(choice=sq_autocomplete)
async def checksq(interaction, choice: str):
    if choice not in client.sq:
        await interaction.response.send_message("Invalid name")
    else:
        if len(client.sq[choice]) == 0:
            await interaction.response.send_message("no one")
        else:
            await interaction.response.send_message(
                ", ".join(str(x) for x in list(client.sq[choice]))
            )
    return


@tree.command()
@app_commands.autocomplete(choice=h_autocomplete)
async def checkh(interaction, choice: str):
    if choice not in client.hangout:
        await interaction.response.send_message("Invalid name")
    else:
        if len(client.hangout[choice]) == 0:
            await interaction.response.send_message("no one")
        else:
            await interaction.response.send_message(
                ", ".join(str(x) for x in list(client.hangout[choice]))
            )
    return


@tree.command()
async def resetaq(interaction):
    client.aq = set()
    with open("archon_quest.pkl", "wb") as f:
        pickle.dump(client.aq, f)
    await interaction.response.send_message("AQ progress reset for everyone")
    return


client.run("")
