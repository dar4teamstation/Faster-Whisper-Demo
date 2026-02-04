# Quick Start Guide

Get up and running with Faster Whisper in under 5 minutes!

## 1. Prerequisites Check

```bash
# Check Python (need 3.8+)
python3 --version

# Check FFmpeg (required)
ffmpeg -version
```

**Don't have FFmpeg?**
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg
```

## 2. Setup (One-Time)

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/Faster-Whisper-Demo.git
cd Faster-Whisper-Demo

# Run setup script
chmod +x setup.sh
./setup.sh
```

That's it! Setup complete.

## 3. Your First Transcription

```bash
# Activate environment
source venv/bin/activate

# Transcribe a video
python transcribe_video.py your_video.mp4
```

**Output:** `your_video.txt` with timestamped transcription

## 4. Common Commands

```bash
# Better quality
python transcribe_video.py video.mp4 --model medium

# Generate subtitles
python transcribe_video.py video.mp4 --format srt

# Both text and subtitles
python transcribe_video.py video.mp4 --format both

# Specify language (faster)
python transcribe_video.py video.mp4 --language en

# GPU acceleration (if available)
python transcribe_video.py video.mp4 --device cuda --compute-type float16
```

## 5. When You're Done

```bash
deactivate
```

## Next Steps

- **See all options:** `python transcribe_video.py --help`
- **More examples:** Check `EXAMPLES.md`
- **Full documentation:** See `README.md`

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "ffmpeg not found" | Install FFmpeg (see step 1) |
| Slow processing | Use `--model tiny` or GPU |
| Poor quality | Use `--model medium` or specify `--language` |
| Out of memory | Use smaller model or CPU |

## Model Quick Reference

- **tiny** - Fastest, 5-10 min for 1hr video
- **base** - Default, 10-20 min for 1hr video ⭐
- **medium** - Best quality, 30-60 min for 1hr video
- **large-v3** - Maximum accuracy, 60-120 min for 1hr video

---

**That's it!** You're ready to transcribe videos. 🎉

For detailed examples and workflows, see `EXAMPLES.md`.
