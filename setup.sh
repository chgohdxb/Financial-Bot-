#!/bin/bash

# Financial Bot Setup Script
# This script sets up the virtual environment and installs dependencies

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$PROJECT_DIR/venv"

echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                   Financial Bot Setup Script                              ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

echo ""
echo "🔄 Activating virtual environment..."
source "$VENV_DIR/bin/activate"
echo "✅ Virtual environment activated"

echo ""
echo "📚 Installing dependencies..."
pip install --upgrade pip
pip install -r "$PROJECT_DIR/requirements.txt"
echo "✅ Dependencies installed"

echo ""
echo "⚙️  Checking environment configuration..."
if [ ! -f "$PROJECT_DIR/.env" ]; then
    echo "📝 Creating .env file from template..."
    cp "$PROJECT_DIR/.env.example" "$PROJECT_DIR/.env"
    echo "⚠️  IMPORTANT: Edit .env file and add your Mistral AI API key"
    echo "   Location: $PROJECT_DIR/.env"
else
    echo "✅ .env file already exists"
fi

echo ""
echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                        Setup Complete! ✅                                 ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""
echo "🚀 To run the bot:"
echo "   1. Make sure you've added your API key to .env"
echo "   2. Run: python bot.py"
echo ""
echo "📖 For help, run: python bot.py"
echo "   Then type: /help"
echo ""
