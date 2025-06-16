import discord
from discord import app_commands, Interaction, File, Embed
from discord.ext import commands
import os
from utils.video_downloader import download_video
from utils.logger import setup_logger

logger = setup_logger(__name__)


class VideoEmbed(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_load(self):
        logger.info("VideoEmbed cog loaded")

    @app_commands.command(name="embed", description="Embed a video from a URL (YouTube, TikTok, Instagram)")
    @app_commands.describe(url="Video link to embed")
    async def embed(self, interaction: Interaction, url: str):
        logger.info(f"Received embed request from {interaction.user} - URL: {url}")
        await interaction.response.defer(thinking=True)

        try:
            video_path = download_video(url)

            file_size = os.path.getsize(video_path)
            if file_size > 25 * 1024 * 1024:  # Discord limit for non-Nitro users
                await interaction.followup.send("❌ Video is too large to upload (25MB limit).")
                os.remove(video_path)
                return

            file = File(video_path, filename="video.mp4")
            embed = Embed(
                title="📽️ Embedded Video",
                description=f"From: {url}",
                color=discord.Color.blurple()
            )

            await interaction.followup.send(file=file, embed=embed)
            logger.info(f"Successfully sent video to {interaction.user}")

            os.remove(video_path)

        except Exception as e:
            logger.error(f"Error processing video: {e}")
            await interaction.followup.send("❌ Failed to process the video.")
