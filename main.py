import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Keep alive web server
app = Flask('')

@app.route('/')
def home():
    return "Disha is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hi baby 😘 I'm Disha, your naughty assistant.")

# Run bot using Replit secret
bot.run(os.environ["TOKEN"])
