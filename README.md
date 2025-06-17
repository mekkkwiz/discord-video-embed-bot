# Discord Video Embed & Team Generator Bot

A feature-rich Discord bot that combines video embedding capabilities with team generation functionality. Built with Python and discord.py, this bot allows users to embed videos from popular platforms and randomly generate teams from lists of people.

## 🌟 Features

### 📽️ Video Embedding
- **Multi-platform support**: YouTube, TikTok, Instagram, and more
- **Smart file handling**: Automatic file size validation (25MB Discord limit)
- **Clean embeds**: Beautiful Discord embeds with video information
- **Safe downloads**: Temporary file management with automatic cleanup

### 🎲 Team Generation
- **Random team creation**: Generate balanced teams from any list of people
- **Smart distribution**: Automatically distributes people as evenly as possible
- **Input validation**: Handles duplicates, spaces, and validates names
- **Rich responses**: Beautiful Discord embeds showing team assignments
- **Flexible sizing**: Support for 1-20 teams with hundreds of participants

### 🔧 Technical Features
- **Slash commands**: Modern Discord slash command interface
- **Comprehensive logging**: Full activity tracking and error monitoring
- **Error handling**: Graceful error recovery with user-friendly messages
- **Modular design**: Clean separation of concerns with cogs and utilities
- **Type hints**: Full type annotation for better code quality

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- UV package manager ([Installation guide](https://docs.astral.sh/uv/getting-started/installation/))
- Discord Bot Token ([Create a bot](https://discord.com/developers/applications))

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd discord-video-embed-bot
   ```

2. **Install dependencies with UV**
   ```bash
   # Create virtual environment and install dependencies
   uv sync
   
   # Activate the virtual environment
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

3. **Set up environment variables**
   ```bash
   # Create .env file
   cp .env.example .env
   
   # Edit .env with your Discord bot token
   echo "DISCORD_TOKEN=your_bot_token_here" > .env
   ```

4. **Run the bot**
   ```bash
   # Using UV (recommended)
   uv run bot.py
   
   # Or with activated virtual environment
   python bot.py
   ```

### Alternative Installation Methods

#### Using pip (traditional)
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the bot
python bot.py
```

#### Development Installation
```bash
# Install with development dependencies
uv sync --dev

# Run tests
uv run python test_teams.py

# Run with development mode
uv run python bot.py
```

## 🎮 Commands

### Video Embedding
- `/embed <url>` - Embed a video from YouTube, TikTok, Instagram, etc.

### Team Generation
- `/teams <num_teams> <num_people> <people_list>` - Generate random teams
- `/teamhelp` - Show detailed help for team commands

### General
- `!ping` - Test bot connectivity (prefix command)

## 📖 Usage Examples

### Video Embedding
```
/embed https://www.youtube.com/watch?v=dQw4w9WgXcQ
/embed https://www.tiktok.com/@user/video/1234567890
```

### Team Generation
```
# Create 2 teams from 6 people
/teams 2 6 Alice,Bob,Charlie,Diana,Eve,Frank

# Create 3 teams from 12 people
/teams 3 12 John,Jane,Mike,Sarah,Tom,Lisa,Dave,Emma,Ryan,Kate,Alex,Sam

# Get help
/teamhelp
```

## 🏗️ Project Structure

```
discord-video-embed-bot/
├── bot.py                 # Main bot entry point
├── pyproject.toml         # UV/pip configuration
├── requirements.txt       # Alternative pip requirements
├── .env                   # Environment variables (not in repo)
├── cogs/                  # Discord bot cogs (features)
│   ├── video_embed.py     # Video embedding functionality
│   └── team_manager.py    # Team generation functionality
├── utils/                 # Utility modules
│   ├── logger.py          # Logging configuration
│   ├── keep_alive.py      # Bot uptime management
│   ├── video_downloader.py # Video download logic
│   └── team_generator.py  # Team generation logic
├── logs/                  # Log files
├── downloads/             # Temporary video storage
└── test_teams.py          # Test suite for team generation
```

## ⚙️ Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
# Discord Bot Token (required)
DISCORD_TOKEN=your_discord_bot_token_here

# Optional: Custom settings
LOG_LEVEL=INFO
MAX_FILE_SIZE=25000000  # 25MB in bytes
```

### Bot Permissions
Your Discord bot needs the following permissions:
- `Send Messages`
- `Use Slash Commands`
- `Attach Files`
- `Embed Links`
- `Read Message History`

### Discord Developer Setup
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to "Bot" section and create a bot
4. Copy the bot token to your `.env` file
5. Go to "OAuth2" > "URL Generator"
6. Select scopes: `bot` and `applications.commands`
7. Select required permissions (listed above)
8. Use the generated URL to invite the bot to your server

## 🛠️ Development

### Setting up Development Environment
```bash
# Clone and setup
git clone <your-repo-url>
cd discord-video-embed-bot

# Install with development dependencies
uv sync --dev

# Activate virtual environment
source .venv/bin/activate
```

### Running Tests
```bash
# Test team generation functionality
uv run python test_teams.py

# Check for syntax errors
uv run python -m py_compile bot.py cogs/*.py utils/*.py
```

### Adding New Features
1. Create new cogs in the `cogs/` directory
2. Add utility functions to the `utils/` directory
3. Update `bot.py` to load new cogs
4. Add tests for new functionality
5. Update documentation

### Code Style
This project follows Python best practices:
- Type hints for all functions
- Comprehensive logging
- Error handling with user feedback
- Modular design with separation of concerns
- Clear documentation and comments

## 📝 Logging

The bot maintains comprehensive logs in `logs/discord-bot.log`:
- Command usage and user activity
- Error tracking and debugging information
- Performance metrics
- Video download and team generation activities

Log levels:
- `INFO`: General bot activity
- `DEBUG`: Detailed operation information
- `ERROR`: Error conditions and exceptions
- `WARNING`: Potential issues

## 🚨 Troubleshooting

### Common Issues

**Bot not responding to commands**
- Check if the bot is online in your Discord server
- Verify the bot has the correct permissions
- Ensure slash commands are synced (happens automatically on startup)

**Video embedding fails**
- Check if the platform is supported by yt-dlp
- Verify the video URL is accessible
- Check file size (Discord limit: 25MB)

**Team generation issues**
- Ensure you have more people than teams
- Check name formatting (comma-separated)
- Verify team count is between 1-20

**Installation issues with UV**
```bash
# Update UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clean installation
rm -rf .venv uv.lock
uv sync
```

### Getting Help
1. Check the logs in `logs/discord-bot.log`
2. Run the test suite: `uv run python test_teams.py`
3. Use `/teamhelp` for team generation help
4. Check Discord bot permissions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Update documentation
6. Submit a pull request

### Development Guidelines
- Follow existing code style and patterns
- Add comprehensive logging for new features
- Include error handling with user-friendly messages
- Write tests for new functionality
- Update documentation

## 📄 License

[Add your license information here]

## 🙏 Acknowledgments

- [discord.py](https://github.com/Rapptz/discord.py) - Discord API wrapper
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Video downloading
- [UV](https://github.com/astral-sh/uv) - Fast Python package manager
- [Flask](https://flask.palletsprojects.com/) - Keep-alive functionality

## 📊 Stats

- **Commands**: 4 slash commands + 1 prefix command
- **Features**: Video embedding + Team generation
- **Platforms**: YouTube, TikTok, Instagram, and more
- **Team Support**: 1-20 teams, unlimited participants
- **Python**: 3.11+ with full type hints

---

**Need help?** Use the `/teamhelp` command in Discord or check the troubleshooting section above.
