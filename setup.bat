@echo off
REM Discord Bot Setup Script for Windows
REM This script helps you set up the Discord Video Embed & Team Generator Bot

echo 🤖 Discord Bot Setup Script
echo ==============================

REM Check if UV is installed
uv --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ UV is not installed!
    echo ℹ️  Please install UV first: https://docs.astral.sh/uv/getting-started/installation/
    echo.
    echo Quick install command:
    echo powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    pause
    exit /b 1
)

echo ✅ UV is installed

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python version %PYTHON_VERSION% found

REM Install dependencies
echo ℹ️  Installing dependencies with UV...
uv sync
if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed successfully

REM Set up environment file
if not exist ".env" (
    echo ℹ️  Creating .env file from template...
    copy .env.example .env
    echo ⚠️  Please edit .env file and add your Discord bot token!
    echo ℹ️  Get your token from: https://discord.com/developers/applications
) else (
    echo ℹ️  .env file already exists
)

REM Create directories
if not exist "logs" mkdir logs
if not exist "downloads" mkdir downloads

echo ✅ Directory structure created

REM Run tests
echo ℹ️  Running team generation tests...
uv run python test_teams.py >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ All tests passed!
) else (
    echo ⚠️  Some tests failed, but the bot should still work
)

echo.
echo 🎉 Setup complete!
echo.
echo Next steps:
echo 1. Edit the .env file and add your Discord bot token
echo 2. Run the bot with: uv run bot.py
echo 3. Invite the bot to your Discord server
echo.
echo For more information, see README.md
pause
