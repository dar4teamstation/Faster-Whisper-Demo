# Contributing to Faster Whisper Demo

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Issues

If you encounter a bug or have a feature request:

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** with a clear title and description
3. **Include details:**
   - Your OS and Python version
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Error messages or logs

### Suggesting Enhancements

We welcome suggestions for improvements:

- New features
- Performance optimizations
- Better documentation
- Additional output formats
- Support for more languages

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Faster-Whisper-Demo.git
   cd Faster-Whisper-Demo
   ```

3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Making Changes

### Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions
- Keep functions focused and modular
- Comment complex logic

### Testing Your Changes

Before submitting:

1. Test with different video formats (mp4, avi, mov)
2. Test with different model sizes (tiny, base, medium)
3. Test both output formats (txt, srt)
4. Verify error handling works correctly
5. Check that help text is accurate

### Example Test Commands

```bash
# Test basic functionality
python transcribe_video.py test_video.mp4

# Test different models
python transcribe_video.py test_video.mp4 --model tiny
python transcribe_video.py test_video.mp4 --model medium

# Test output formats
python transcribe_video.py test_video.mp4 --format srt
python transcribe_video.py test_video.mp4 --format both

# Test error handling
python transcribe_video.py nonexistent.mp4
```

## Submitting Changes

1. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Add: Brief description of changes"
   ```

2. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request:**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Provide a clear description of changes
   - Reference any related issues

### Pull Request Guidelines

- **Clear title** describing the change
- **Detailed description** of what and why
- **Link related issues** using #issue_number
- **Keep changes focused** - one feature/fix per PR
- **Update documentation** if needed
- **Test thoroughly** before submitting

## Commit Message Format

Use clear, descriptive commit messages:

```
Add: New feature description
Fix: Bug fix description
Update: Documentation or dependency updates
Refactor: Code improvements without changing functionality
```

Examples:
```
Add: Support for WebM video format
Fix: Handle videos with no audio track
Update: README with GPU setup instructions
Refactor: Extract audio processing to separate function
```

## Areas for Contribution

### High Priority

- [ ] Add support for more video formats
- [ ] Improve error messages and handling
- [ ] Add progress bars for long transcriptions
- [ ] Support for batch processing multiple files
- [ ] Add unit tests

### Medium Priority

- [ ] Support for custom vocabulary/terminology
- [ ] Add speaker diarization (who said what)
- [ ] Export to more formats (JSON, VTT, etc.)
- [ ] GUI interface option
- [ ] Docker container support

### Documentation

- [ ] More usage examples
- [ ] Video tutorials
- [ ] Troubleshooting guide expansion
- [ ] Performance benchmarks
- [ ] Language-specific guides

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

## Questions?

Feel free to:
- Open an issue for questions
- Start a discussion
- Reach out to maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to make this project better! 🎉
