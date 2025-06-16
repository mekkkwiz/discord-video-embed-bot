import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

from cogs.video_embed import VideoEmbed
from utils.logger import setup_logger

# Load environment variables from .env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
if not token:
    raise ValueError("DISCORD_TOKEN not found in .env")

# Setup logger
logger = setup_logger("bot")

# Configure intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Only needed if your bot interacts with member lists

# Initialize bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Slash command sync on ready
@bot.event
async def on_ready():
    logger.info(f"✅ Bot connected as {bot.user} (ID: {bot.user.id})")

    try:
        await bot.tree.sync()
        logger.info("✅ Slash commands synced globally")
    except Exception as e:
        logger.error(f"❌ Failed to sync slash commands: {e}")


# Error handler for classic commands
@bot.event
async def on_command_error(ctx, error):
    logger.error(f"❌ Error in command '{ctx.command}': {error}")
    await ctx.send("An error occurred while processing your command.")

# Test prefix command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
    logger.info(f"Ping command used by {ctx.author} in {ctx.guild.name if ctx.guild else 'DM'}")

# Setup function to load cogs
async def setup():
    await bot.add_cog(VideoEmbed(bot))

# Entry point
async def main():
    async with bot:
        await setup()
        await bot.start(token)

# Run the bot
asyncio.run(main())