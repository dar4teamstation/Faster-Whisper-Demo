#!/usr/bin/env python3
"""
Video Transcription Script using Faster Whisper
Supports long videos (up to 1 hour or more) with efficient processing
"""

import os
import sys
import argparse
from pathlib import Path
from faster_whisper import WhisperModel
import subprocess
import tempfile
from datetime import timedelta


def extract_audio(video_path, audio_path):
    """
    Extract audio from video file using ffmpeg
    
    Args:
        video_path: Path to input video file
        audio_path: Path to output audio file
    """
    print(f"Extracting audio from video...")
    cmd = [
        'ffmpeg',
        '-i', video_path,
        '-vn',  # No video
        '-acodec', 'pcm_s16le',  # PCM 16-bit
        '-ar', '16000',  # 16kHz sample rate (optimal for Whisper)
        '-ac', '1',  # Mono
        '-y',  # Overwrite output file
        audio_path
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"Audio extracted successfully to: {audio_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error extracting audio: {e.stderr.decode()}")
        raise


def format_timestamp(seconds):
    """Convert seconds to HH:MM:SS.mmm format"""
    td = timedelta(seconds=seconds)
    hours = td.seconds // 3600
    minutes = (td.seconds % 3600) // 60
    secs = td.seconds % 60
    millis = td.microseconds // 1000
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{millis:03d}"


def transcribe_audio(audio_path, model_size="base", device="cpu", compute_type="int8", language=None):
    """
    Transcribe audio file using Faster Whisper
    
    Args:
        audio_path: Path to audio file
        model_size: Whisper model size (tiny, base, small, medium, large-v2, large-v3)
        device: Device to use (cpu, cuda)
        compute_type: Computation type (int8, float16, float32)
        language: Language code (None for auto-detection)
    
    Returns:
        List of transcription segments
    """
    print(f"Loading Whisper model: {model_size}")
    model = WhisperModel(model_size, device=device, compute_type=compute_type)
    
    print(f"Transcribing audio (this may take a while for long videos)...")
    
    # Transcribe with word-level timestamps for better accuracy
    segments, info = model.transcribe(
        audio_path,
        language=language,
        beam_size=5,
        vad_filter=True,  # Voice Activity Detection to filter out silence
        vad_parameters=dict(min_silence_duration_ms=500),
        word_timestamps=True
    )
    
    print(f"Detected language: {info.language} (probability: {info.language_probability:.2f})")
    
    return segments, info


def save_transcription(segments, output_path, include_timestamps=True):
    """
    Save transcription to file
    
    Args:
        segments: Transcription segments from Whisper
        output_path: Path to output text file
        include_timestamps: Whether to include timestamps in output
    """
    print(f"Saving transcription to: {output_path}")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for segment in segments:
            if include_timestamps:
                start_time = format_timestamp(segment.start)
                end_time = format_timestamp(segment.end)
                f.write(f"[{start_time} --> {end_time}]\n")
            f.write(f"{segment.text.strip()}\n\n")
    
    print(f"Transcription saved successfully!")


def save_srt(segments, output_path):
    """
    Save transcription in SRT subtitle format
    
    Args:
        segments: Transcription segments from Whisper
        output_path: Path to output SRT file
    """
    print(f"Saving SRT subtitles to: {output_path}")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, segment in enumerate(segments, start=1):
            start_time = format_timestamp(segment.start).replace('.', ',')
            end_time = format_timestamp(segment.end).replace('.', ',')
            f.write(f"{i}\n")
            f.write(f"{start_time} --> {end_time}\n")
            f.write(f"{segment.text.strip()}\n\n")
    
    print(f"SRT subtitles saved successfully!")


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe video files using Faster Whisper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage with default settings
  python transcribe_video.py video.mp4

  # Use a larger model for better accuracy
  python transcribe_video.py video.mp4 --model medium

  # Specify language and output format
  python transcribe_video.py video.mp4 --language en --format both

  # Use GPU acceleration (requires CUDA)
  python transcribe_video.py video.mp4 --device cuda --compute-type float16

Model sizes (accuracy vs speed):
  - tiny: Fastest, least accurate
  - base: Good balance (default)
  - small: Better accuracy
  - medium: High accuracy, slower
  - large-v2/large-v3: Best accuracy, slowest
        """
    )
    
    parser.add_argument('video_path', help='Path to video file')
    parser.add_argument('--model', default='base', 
                       choices=['tiny', 'base', 'small', 'medium', 'large-v2', 'large-v3'],
                       help='Whisper model size (default: base)')
    parser.add_argument('--device', default='cpu', choices=['cpu', 'cuda'],
                       help='Device to use (default: cpu)')
    parser.add_argument('--compute-type', default='int8',
                       choices=['int8', 'float16', 'float32'],
                       help='Computation type (default: int8)')
    parser.add_argument('--language', default=None,
                       help='Language code (e.g., en, es, fr). Auto-detect if not specified')
    parser.add_argument('--output', '-o', default=None,
                       help='Output file path (default: same as video with .txt extension)')
    parser.add_argument('--format', default='txt', choices=['txt', 'srt', 'both'],
                       help='Output format (default: txt)')
    parser.add_argument('--no-timestamps', action='store_true',
                       help='Exclude timestamps from text output')
    parser.add_argument('--keep-audio', action='store_true',
                       help='Keep extracted audio file')
    
    args = parser.parse_args()
    
    # Validate input file
    video_path = Path(args.video_path)
    if not video_path.exists():
        print(f"Error: Video file not found: {video_path}")
        sys.exit(1)
    
    # Determine output paths
    if args.output:
        output_base = Path(args.output).with_suffix('')
    else:
        output_base = video_path.with_suffix('')
    
    output_txt = f"{output_base}.txt"
    output_srt = f"{output_base}.srt"
    
    # Create temporary audio file
    temp_audio = None
    try:
        # Extract audio
        if args.keep_audio:
            audio_path = f"{output_base}.wav"
        else:
            temp_audio = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
            audio_path = temp_audio.name
            temp_audio.close()
        
        extract_audio(str(video_path), audio_path)
        
        # Transcribe
        segments, info = transcribe_audio(
            audio_path,
            model_size=args.model,
            device=args.device,
            compute_type=args.compute_type,
            language=args.language
        )
        
        # Convert generator to list to allow multiple iterations
        segments_list = list(segments)
        
        # Save transcription
        if args.format in ['txt', 'both']:
            save_transcription(segments_list, output_txt, include_timestamps=not args.no_timestamps)
        
        if args.format in ['srt', 'both']:
            save_srt(segments_list, output_srt)
        
        print("\n" + "="*50)
        print("Transcription completed successfully!")
        print("="*50)
        if args.format in ['txt', 'both']:
            print(f"Text output: {output_txt}")
        if args.format in ['srt', 'both']:
            print(f"SRT output: {output_srt}")
        if args.keep_audio:
            print(f"Audio file: {audio_path}")
        
    except Exception as e:
        print(f"\nError during transcription: {e}")
        sys.exit(1)
    
    finally:
        # Clean up temporary audio file
        if temp_audio and not args.keep_audio:
            try:
                os.unlink(audio_path)
            except:
                pass


if __name__ == "__main__":
    main()
