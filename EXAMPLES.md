# Usage Examples

This document provides detailed examples for common use cases.

## Table of Contents

- [Basic Transcription](#basic-transcription)
- [Different Model Sizes](#different-model-sizes)
- [Output Formats](#output-formats)
- [Language Options](#language-options)
- [GPU Acceleration](#gpu-acceleration)
- [Batch Processing](#batch-processing)
- [Common Workflows](#common-workflows)

## Basic Transcription

### Simple transcription with default settings

```bash
python transcribe_video.py lecture.mp4
```

**Output:** `lecture.txt` with timestamps

**Best for:** Quick transcriptions, testing

---

## Different Model Sizes

### Tiny - Fastest (for quick drafts)

```bash
python transcribe_video.py meeting.mp4 --model tiny
```

**Processing time:** ~5-10 min for 1 hour video  
**Best for:** Quick drafts, low-priority content

### Base - Balanced (default)

```bash
python transcribe_video.py presentation.mp4 --model base
```

**Processing time:** ~10-20 min for 1 hour video  
**Best for:** Most use cases, good balance

### Medium - High Quality

```bash
python transcribe_video.py interview.mp4 --model medium
```

**Processing time:** ~30-60 min for 1 hour video  
**Best for:** Professional transcriptions, important content

### Large - Best Quality

```bash
python transcribe_video.py podcast.mp4 --model large-v3
```

**Processing time:** ~60-120 min for 1 hour video  
**Best for:** Critical content, maximum accuracy needed

---

## Output Formats

### Text only (with timestamps)

```bash
python transcribe_video.py video.mp4 --format txt
```

**Output:** `video.txt`

### SRT subtitles only

```bash
python transcribe_video.py video.mp4 --format srt
```

**Output:** `video.srt` (can be used with video players)

### Both formats

```bash
python transcribe_video.py video.mp4 --format both
```

**Output:** `video.txt` and `video.srt`

### Text without timestamps

```bash
python transcribe_video.py video.mp4 --no-timestamps
```

**Output:** Plain text without time markers

---

## Language Options

### Auto-detect language (default)

```bash
python transcribe_video.py video.mp4
```

The model will automatically detect the language.

### Specify language for better accuracy

```bash
# English
python transcribe_video.py video.mp4 --language en

# Spanish
python transcribe_video.py video.mp4 --language es

# French
python transcribe_video.py video.mp4 --language fr

# German
python transcribe_video.py video.mp4 --language de

# Japanese
python transcribe_video.py video.mp4 --language ja

# Chinese
python transcribe_video.py video.mp4 --language zh
```

**Tip:** Specifying the language is faster and more accurate than auto-detection.

---

## GPU Acceleration

### Use GPU with CUDA (requires NVIDIA GPU)

```bash
python transcribe_video.py video.mp4 --device cuda --compute-type float16
```

**Speed improvement:** 5-10x faster than CPU

### Different compute types

```bash
# Float16 (fastest on GPU, good quality)
python transcribe_video.py video.mp4 --device cuda --compute-type float16

# Float32 (slower, slightly better quality)
python transcribe_video.py video.mp4 --device cuda --compute-type float32

# Int8 (CPU optimized, default)
python transcribe_video.py video.mp4 --device cpu --compute-type int8
```

---

## Batch Processing

### Process multiple videos

Create a simple bash script:

```bash
#!/bin/bash
# batch_transcribe.sh

for video in *.mp4; do
    echo "Processing: $video"
    python transcribe_video.py "$video" --model base --format both
done
```

Run it:

```bash
chmod +x batch_transcribe.sh
./batch_transcribe.sh
```

### Process with different settings per video

```bash
# Quick transcription for all videos
for video in *.mp4; do
    python transcribe_video.py "$video" --model tiny
done

# High-quality for specific videos
python transcribe_video.py important1.mp4 --model large-v2 --format both
python transcribe_video.py important2.mp4 --model large-v2 --format both
```

---

## Common Workflows

### Workflow 1: Conference Recording

```bash
# High quality with subtitles
python transcribe_video.py conference.mp4 \
    --model medium \
    --format both \
    --language en
```

### Workflow 2: Podcast Episode

```bash
# Best quality, keep audio for editing
python transcribe_video.py podcast_ep01.mp4 \
    --model large-v3 \
    --format both \
    --language en \
    --keep-audio
```

### Workflow 3: Quick Meeting Notes

```bash
# Fast transcription, text only
python transcribe_video.py meeting.mp4 \
    --model tiny \
    --format txt \
    --no-timestamps
```

### Workflow 4: YouTube Video with Subtitles

```bash
# Generate SRT for upload
python transcribe_video.py youtube_video.mp4 \
    --model base \
    --format srt \
    --language en
```

### Workflow 5: Multi-language Content

```bash
# Spanish content
python transcribe_video.py spanish_video.mp4 \
    --model medium \
    --language es \
    --format both

# Japanese content
python transcribe_video.py japanese_video.mp4 \
    --model medium \
    --language ja \
    --format both
```

### Workflow 6: Testing Before Full Processing

```bash
# Step 1: Quick test with tiny model
python transcribe_video.py long_video.mp4 --model tiny

# Step 2: Review quality, then process with better model
python transcribe_video.py long_video.mp4 --model medium --format both
```

---

## Custom Output Locations

### Save to specific directory

```bash
python transcribe_video.py video.mp4 --output transcripts/video_transcript.txt
```

### Organize by date

```bash
mkdir -p transcripts/$(date +%Y-%m-%d)
python transcribe_video.py video.mp4 --output transcripts/$(date +%Y-%m-%d)/video.txt
```

---

## Performance Optimization

### For very long videos (2+ hours)

```bash
# Use GPU if available
python transcribe_video.py long_video.mp4 \
    --device cuda \
    --compute-type float16 \
    --model base

# Or use smaller model on CPU
python transcribe_video.py long_video.mp4 \
    --model tiny
```

### For best accuracy on difficult audio

```bash
python transcribe_video.py difficult_audio.mp4 \
    --model large-v3 \
    --language en \
    --format both
```

---

## Troubleshooting Examples

### If transcription is too slow

```bash
# Use smaller model
python transcribe_video.py video.mp4 --model tiny

# Or use GPU
python transcribe_video.py video.mp4 --device cuda --compute-type float16
```

### If quality is poor

```bash
# Use larger model and specify language
python transcribe_video.py video.mp4 --model medium --language en
```

### If running out of memory

```bash
# Use smaller model with CPU
python transcribe_video.py video.mp4 --model base --device cpu --compute-type int8
```

---

## Tips

1. **Always start with `base` model** - It's the sweet spot for most use cases
2. **Specify language when known** - Faster and more accurate
3. **Use `--format both`** - Get both text and SRT files
4. **Test with `tiny` first** - For very long videos, test quality before full processing
5. **Keep audio with `--keep-audio`** - Useful if you need to re-process later
6. **Use GPU when available** - Dramatically faster processing

---

## Need Help?

Run the help command to see all available options:

```bash
python transcribe_video.py --help
```
