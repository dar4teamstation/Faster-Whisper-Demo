# Faster Whisper Video Transcription Demo

A ready-to-use Python script for transcribing long videos (1+ hours) using OpenAI's Whisper model via the optimized Faster Whisper implementation.

## ✨ Features

- 🎬 **Automatic audio extraction** from video files using FFmpeg
- ⚡ **Optimized for long videos** with Voice Activity Detection (VAD)
- 📝 **Multiple output formats**: Plain text with timestamps or SRT subtitles
- 🎯 **Multiple model sizes** for accuracy vs speed tradeoff
- 🚀 **GPU acceleration** support (optional)
- 🌍 **Automatic language detection** or manual specification
- 💾 **Low memory footprint** compared to standard Whisper

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+**
2. **FFmpeg** (required for audio extraction)

**Install FFmpeg:**
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

### Installation

1. **Clone this repository:**
```bash
git clone https://github.com/YOUR_USERNAME/Faster-Whisper-Demo.git
cd Faster-Whisper-Demo
```

2. **Run the setup script:**
```bash
chmod +x setup.sh
./setup.sh
```

Or manually:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **You're ready to transcribe!**

## 📖 Usage

### Basic Example

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate

# Transcribe a video with default settings
python transcribe_video.py your_video.mp4
```

This creates `your_video.txt` with timestamped transcription.

### Advanced Examples

```bash
# Use a larger model for better accuracy
python transcribe_video.py video.mp4 --model medium

# Generate SRT subtitles
python transcribe_video.py video.mp4 --format srt

# Generate both text and SRT
python transcribe_video.py video.mp4 --format both

# Specify language (faster than auto-detection)
python transcribe_video.py video.mp4 --language en

# Custom output location
python transcribe_video.py video.mp4 --output transcripts/my_transcript.txt

# GPU acceleration (requires CUDA)
python transcribe_video.py video.mp4 --device cuda --compute-type float16

# Keep the extracted audio file
python transcribe_video.py video.mp4 --keep-audio
```

### All Options

```bash
python transcribe_video.py --help
```

## 🎯 Model Selection

| Model | Speed | Accuracy | Memory | Best For |
|-------|-------|----------|--------|----------|
| `tiny` | ⚡⚡⚡⚡⚡ | ⭐⭐ | ~1 GB | Quick drafts, testing |
| `base` | ⚡⚡⚡⚡ | ⭐⭐⭐ | ~1 GB | **Default - balanced** |
| `small` | ⚡⚡⚡ | ⭐⭐⭐⭐ | ~2 GB | Good quality |
| `medium` | ⚡⚡ | ⭐⭐⭐⭐⭐ | ~5 GB | Professional use |
| `large-v2` | ⚡ | ⭐⭐⭐⭐⭐ | ~10 GB | Maximum accuracy |
| `large-v3` | ⚡ | ⭐⭐⭐⭐⭐ | ~10 GB | Latest & best |

### Processing Time Estimates (1 hour video)

**CPU (Intel i7/M1):**
- tiny: ~5-10 minutes
- base: ~10-20 minutes
- medium: ~30-60 minutes

**GPU (NVIDIA RTX 3080):**
- base: ~2-5 minutes
- medium: ~5-10 minutes

## 📄 Output Formats

### Text Format (`.txt`)
```
[00:00:00.000 --> 00:00:05.000]
Welcome to this video tutorial.

[00:00:05.000 --> 00:00:10.000]
Today we'll discuss video transcription.
```

### SRT Subtitle Format (`.srt`)
```
1
00:00:00,000 --> 00:00:05,000
Welcome to this video tutorial.

2
00:00:05,000 --> 00:00:10,000
Today we'll discuss video transcription.
```

## 🔧 Troubleshooting

### "ffmpeg not found"
Install FFmpeg using the instructions in the Prerequisites section.

### Out of memory errors
- Use a smaller model: `--model tiny` or `--model base`
- Use CPU instead of GPU: `--device cpu`

### Poor transcription quality
- Use a larger model: `--model medium` or `--model large-v2`
- Specify language explicitly: `--language en`
- Ensure good audio quality in source video

### Slow processing
- Use smaller model: `--model tiny`
- Enable GPU if available: `--device cuda --compute-type float16`
- VAD filtering is enabled by default to skip silence

## 💡 Tips for Best Results

1. **Start with `base` model** - Good balance for most use cases
2. **Specify language** if known - Faster and more accurate than auto-detection
3. **Use GPU** if available - 5-10x faster than CPU
4. **Check audio quality** - Clear audio = better transcription
5. **Use `--format both`** - Get both text and SRT files

## 🔄 Workflow Example

```bash
# 1. Activate environment
source venv/bin/activate

# 2. Quick test with tiny model
python transcribe_video.py sample.mp4 --model tiny

# 3. If quality is good enough, process full video
python transcribe_video.py full_video.mp4 --model base --format both

# 4. For critical content, use best quality
python transcribe_video.py important.mp4 --model large-v2 --language en --format both

# 5. Deactivate when done
deactivate
```

## 📦 What's Included

- `transcribe_video.py` - Main transcription script
- `requirements.txt` - Python dependencies
- `setup.sh` - Automated setup script
- `README.md` - This file

## 🤝 Contributing

Feel free to open issues or submit pull requests for improvements!

## 📝 License

This project uses Faster Whisper and FFmpeg. Please refer to their respective licenses.

## 🙏 Credits

- [Faster Whisper](https://github.com/guillaumekln/faster-whisper) - Optimized Whisper implementation
- [OpenAI Whisper](https://github.com/openai/whisper) - Original Whisper model
- [FFmpeg](https://ffmpeg.org/) - Audio/video processing

---

**Need help?** Open an issue or check the [Faster Whisper documentation](https://github.com/guillaumekln/faster-whisper)