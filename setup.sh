#!/bin/bash

# Discord Bot Setup Script
# This script helps you set up the Discord Video Embed & Team Generator Bot

set -e  # Exit on any error

echo "🤖 Discord Bot Setup Script"
echo "=============================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if UV is installed
if ! command -v uv &> /dev/null; then
    print_error "UV is not installed!"
    print_info "Please install UV first: https://docs.astral.sh/uv/getting-started/installation/"
    echo
    echo "Quick install command:"
    echo "curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

print_status "UV is installed"

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
REQUIRED_VERSION="3.11"

if [[ $(echo "$PYTHON_VERSION < $REQUIRED_VERSION" | bc -l) -eq 1 ]]; then
    print_error "Python $REQUIRED_VERSION or higher is required. Found: $PYTHON_VERSION"
    exit 1
fi

print_status "Python version $PYTHON_VERSION is compatible"

# Install dependencies
print_info "Installing dependencies with UV..."
uv sync

print_status "Dependencies installed successfully"

# Set up environment file
if [ ! -f ".env" ]; then
    print_info "Creating .env file from template..."
    cp .env.example .env
    print_warning "Please edit .env file and add your Discord bot token!"
    print_info "Get your token from: https://discord.com/developers/applications"
else
    print_info ".env file already exists"
fi

# Create directories
mkdir -p logs downloads

print_status "Directory structure created"

# Run tests
print_info "Running team generation tests..."
if uv run python test_teams.py > /dev/null 2>&1; then
    print_status "All tests passed!"
else
    print_warning "Some tests failed, but the bot should still work"
fi

echo
echo "🎉 Setup complete!"
echo
echo "Next steps:"
echo "1. Edit the .env file and add your Discord bot token"
echo "2. Run the bot with: uv run bot.py"
echo "3. Invite the bot to your Discord server"
echo
echo "For more information, see README.md"
