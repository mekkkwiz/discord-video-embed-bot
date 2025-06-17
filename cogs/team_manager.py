import discord
from discord import app_commands, Interaction, Embed
from discord.ext import commands
from typing import List
import asyncio

from utils.team_generator import generate_teams, validate_team_input
from utils.logger import setup_logger

logger = setup_logger(__name__)


class TeamManager(commands.Cog):
    """Cog for managing team generation and related functionality."""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_load(self):
        logger.info("TeamManager cog loaded")

    @app_commands.command(
        name="teams", 
        description="Generate random teams from a list of people"
    )
    @app_commands.describe(
        num_teams="Number of teams to create",
        num_people="Total number of people (for validation)",
        people_list="Comma-separated list of people names"
    )
    async def generate_teams_command(
        self, 
        interaction: Interaction, 
        num_teams: int, 
        num_people: int, 
        people_list: str
    ):
        """
        Generate random teams from a list of people.
        
        Usage: /teams <num_teams> <num_people> <comma,separated,names>
        Example: /teams 2 10 Alice,Bob,Charlie,Diana,Eve,Frank,Grace,Henry,Ivy,Jack
        """
        logger.info(f"Team generation request from {interaction.user} - "
                   f"{num_teams} teams, {num_people} people expected")
        
        await interaction.response.defer(thinking=True)
        
        try:
            # Validate input parameters
            if num_teams <= 0:
                await interaction.followup.send("❌ Number of teams must be positive!")
                return
            
            if num_people <= 0:
                await interaction.followup.send("❌ Number of people must be positive!")
                return
            
            if num_teams > 20:  # Reasonable limit for Discord embed
                await interaction.followup.send("❌ Maximum 20 teams allowed!")
                return
            
            # Parse and validate people list
            try:
                people = validate_team_input(people_list)
            except ValueError as e:
                await interaction.followup.send(f"❌ Invalid people list: {str(e)}")
                return
            
            # Check if provided num_people matches actual count
            if len(people) != num_people:
                embed = Embed(
                    title="⚠️ People Count Mismatch",
                    description=f"You specified {num_people} people but provided {len(people)} names.\n"
                               f"Proceeding with {len(people)} people.",
                    color=discord.Color.orange()
                )
                await interaction.followup.send(embed=embed)
                await asyncio.sleep(2)  # Give user time to read the warning
            
            # Generate teams
            try:
                result = generate_teams(people, num_teams)
            except ValueError as e:
                await interaction.followup.send(f"❌ Cannot generate teams: {str(e)}")
                return
            
            # Create embed with team results
            embed = await self._create_teams_embed(result, interaction.user)
            
            await interaction.followup.send(embed=embed)
            
            logger.info(f"Successfully generated teams for {interaction.user} - "
                       f"{result['num_teams']} teams with {result['total_people']} people")
            
        except Exception as e:
            logger.error(f"Error in teams command: {e}", exc_info=True)
            await interaction.followup.send("❌ An unexpected error occurred while generating teams.")

    async def _create_teams_embed(self, result: dict, user: discord.User) -> Embed:
        """Create a Discord embed with team generation results."""
        embed = Embed(
            title="🎲 Random Teams Generated!",
            color=discord.Color.green(),
            timestamp=discord.utils.utcnow()
        )
        
        embed.set_footer(text=f"Requested by {user.display_name}", icon_url=user.display_avatar.url)
        
        # Add summary information
        embed.add_field(
            name="📊 Summary",
            value=f"**Total People:** {result['total_people']}\n"
                  f"**Number of Teams:** {result['num_teams']}\n"
                  f"**Team Size Range:** {result['min_team_size']}-{result['max_team_size']} people",
            inline=False
        )
        
        # Add each team
        teams = result["teams"]
        for team_name, members in teams.items():
            if members:  # Only show non-empty teams
                members_list = "\n".join(f"• {member}" for member in members)
                embed.add_field(
                    name=f"👥 {team_name} ({len(members)} members)",
                    value=members_list,
                    inline=True
                )
        
        # Add a tip if teams are uneven
        if result['max_team_size'] > result['min_team_size']:
            embed.add_field(
                name="💡 Note",
                value="Teams have different sizes due to uneven distribution of people.",
                inline=False
            )
        
        return embed

    @app_commands.command(
        name="teamhelp",
        description="Show help for team generation commands"
    )
    async def team_help(self, interaction: Interaction):
        """Display help information for team generation."""
        logger.info(f"Team help requested by {interaction.user}")
        
        embed = Embed(
            title="🎲 Team Generator Help",
            description="Generate random teams from a list of people!",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="📝 Command Usage",
            value="`/teams <num_teams> <num_people> <people_list>`",
            inline=False
        )
        
        embed.add_field(
            name="📋 Parameters",
            value="• **num_teams**: Number of teams to create (1-20)\n"
                  "• **num_people**: Total number of people (for validation)\n"
                  "• **people_list**: Comma-separated names",
            inline=False
        )
        
        embed.add_field(
            name="💡 Example",
            value="`/teams 2 6 Alice,Bob,Charlie,Diana,Eve,Frank`\n"
                  "This creates 2 teams from 6 people.",
            inline=False
        )
        
        embed.add_field(
            name="📌 Tips",
            value="• Names are automatically cleaned and deduplicated\n"
                  "• Teams are distributed as evenly as possible\n"
                  "• Maximum 20 teams and 100 characters per name\n"
                  "• Duplicate names will be removed automatically",
            inline=False
        )
        
        embed.set_footer(text="Need more help? Contact the bot administrator.")
        
        await interaction.response.send_message(embed=embed)

    @generate_teams_command.error
    async def teams_command_error(self, interaction: Interaction, error: app_commands.AppCommandError):
        """Handle errors for the teams command."""
        logger.error(f"Error in teams command for {interaction.user}: {error}")
        
        if interaction.response.is_done():
            await interaction.followup.send("❌ An error occurred while processing your command.")
        else:
            await interaction.response.send_message("❌ An error occurred while processing your command.")
