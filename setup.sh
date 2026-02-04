#!/bin/bash

# Setup script for Faster Whisper Video Transcription Demo
set -e

echo "================================================"
echo "Faster Whisper Setup"
echo "================================================"
echo ""

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "Please install Python 3.8 or higher and try again."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✓ Found Python $PYTHON_VERSION"

# Check for FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  Warning: FFmpeg is not installed."
    echo "FFmpeg is required for audio extraction."
    echo ""
    echo "Install it with:"
    echo "  macOS:   brew install ffmpeg"
    echo "  Ubuntu:  sudo apt-get install ffmpeg"
    echo "  Windows: Download from https://ffmpeg.org/download.html"
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo "✓ Found FFmpeg"
fi

echo ""
echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip -q

echo "Installing dependencies..."
pip install -r requirements.txt -q

echo ""
echo "================================================"
echo "✓ Setup Complete!"
echo "================================================"
echo ""
echo "Quick Start:"
echo "  1. Activate the virtual environment:"
echo "     source venv/bin/activate"
echo ""
echo "  2. Transcribe a video:"
echo "     python transcribe_video.py your_video.mp4"
echo ""
echo "  3. For more options:"
echo "     python transcribe_video.py --help"
echo ""
echo "  4. When done, deactivate:"
echo "     deactivate"
echo ""
echo "Example with all features:"
echo "  python transcribe_video.py video.mp4 --model medium --format both --language en"
echo ""
