# Contributing to Discord Video Embed & Team Generator Bot

Thank you for your interest in contributing to this Discord bot! This document provides guidelines for contributing to the project.

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher
- UV package manager
- Git
- A Discord bot token for testing

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/discord-video-embed-bot.git
   cd discord-video-embed-bot
   ```

2. **Set up development environment**
   ```bash
   # Run the setup script
   ./setup.sh  # Linux/macOS
   # or
   setup.bat   # Windows
   
   # Or manually:
   uv sync --dev
   cp .env.example .env
   # Edit .env with your test bot token
   ```

3. **Run tests**
   ```bash
   uv run python test_teams.py
   ```

## 🏗️ Project Structure

```
discord-video-embed-bot/
├── bot.py                 # Main bot entry point
├── cogs/                  # Discord bot features (commands)
│   ├── video_embed.py     # Video embedding functionality
│   └── team_manager.py    # Team generation functionality
├── utils/                 # Utility functions
│   ├── logger.py          # Logging setup
│   ├── keep_alive.py      # Bot uptime management
│   ├── video_downloader.py # Video download logic
│   └── team_generator.py  # Team generation logic
└── test_teams.py          # Test suite
```

## 📝 Coding Standards

### Python Style Guide
- Follow PEP 8 style guidelines
- Use type hints for all functions and methods
- Maximum line length: 88 characters
- Use Black for code formatting
- Use isort for import sorting

### Code Organization
- **Cogs**: Discord-specific functionality (commands, events)
- **Utils**: Reusable utility functions and classes
- **Tests**: Test files should be comprehensive and cover edge cases

### Naming Conventions
- Functions and variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Files: `snake_case.py`

### Documentation
- Add docstrings to all functions and classes
- Use type hints extensively
- Comment complex logic
- Update README.md for new features

## 🔄 Development Workflow

### 1. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes
- Follow the coding standards above
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes
```bash
# Run existing tests
uv run python test_teams.py

# Test the bot manually with your Discord server
uv run bot.py

# Check code quality (if dev dependencies installed)
uv run black . --check
uv run isort . --check-only
uv run flake8 .
```

### 4. Commit Your Changes
```bash
git add .
git commit -m "feat: add new feature description"
```

Use conventional commit messages:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `refactor:` for code refactoring
- `test:` for adding tests
- `chore:` for maintenance tasks

### 5. Submit a Pull Request
1. Push your branch to your fork
2. Create a pull request to the main repository
3. Describe your changes in the PR description
4. Wait for review and address feedback

## 🐛 Bug Reports

When reporting bugs, please include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Bot logs (remove sensitive information)
- Environment details (Python version, OS, etc.)

## 💡 Feature Requests

For new feature requests:
- Check if the feature already exists
- Describe the use case clearly
- Explain why it would be valuable
- Consider implementation complexity

## 🧪 Testing Guidelines

### Test Coverage
- Add tests for new functionality
- Test edge cases and error conditions
- Ensure existing tests still pass

### Test Types
- **Unit tests**: Test individual functions
- **Integration tests**: Test component interactions
- **Manual tests**: Test Discord bot functionality

### Running Tests
```bash
# Run team generation tests
uv run python test_teams.py

# Run with verbose output
uv run python test_teams.py -v
```

## 📚 Adding New Features

### Adding a New Command
1. Create or modify a cog in `cogs/`
2. Add utility functions in `utils/` if needed
3. Update `bot.py` to load new cogs
4. Add comprehensive logging
5. Include error handling
6. Write tests
7. Update documentation

### Example: Adding a New Cog
```python
# cogs/new_feature.py
import discord
from discord import app_commands, Interaction
from discord.ext import commands
from utils.logger import setup_logger

logger = setup_logger(__name__)

class NewFeature(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    async def cog_load(self):
        logger.info("NewFeature cog loaded")
    
    @app_commands.command(name="newcommand", description="Description")
    async def new_command(self, interaction: Interaction):
        logger.info(f"New command used by {interaction.user}")
        # Implementation here
```

### Adding Utility Functions
```python
# utils/new_utility.py
from typing import Any
from utils.logger import setup_logger

logger = setup_logger(__name__)

def utility_function(param: str) -> Any:
    """
    Description of the function.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When invalid input is provided
    """
    logger.debug(f"Processing: {param}")
    # Implementation here
```

## 🔒 Security Guidelines

- Never commit tokens, passwords, or sensitive data
- Use environment variables for configuration
- Validate all user inputs
- Handle errors gracefully without exposing internals
- Follow Discord's Terms of Service and API guidelines

## 📋 Code Review Checklist

Before submitting a PR, ensure:
- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New functionality is tested
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No sensitive data is exposed
- [ ] Error handling is comprehensive
- [ ] Logging is appropriate

## 🙋‍♂️ Getting Help

If you need help:
1. Check existing documentation
2. Look at similar implementations in the codebase
3. Open an issue for discussion
4. Join our Discord server (if available)

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

Thank you for contributing! 🎉
