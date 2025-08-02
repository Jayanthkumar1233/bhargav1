# Text to Speech Converter

A modern web application that converts text or text files into downloadable MP3 audio files with customizable tones.

## Features

- **Text Input**: Directly type or paste text for conversion
- **File Upload**: Upload .txt files for batch processing
- **Multiple Tones**: Choose from three different speech tones:
  - **Neutral**: Standard, clear speech
  - **Suspenseful**: Slower pace with dramatic pauses
  - **Inspiring**: Emphasized speech with clear pronunciation
- **Downloadable MP3**: Get high-quality audio files ready for download
- **Modern UI**: Beautiful, responsive design with smooth animations
- **File Management**: Automatic cleanup of generated files

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## Usage

### Text Input Mode
1. Click on the "Text Input" tab
2. Type or paste your text in the textarea
3. Select your preferred tone (Neutral, Suspenseful, or Inspiring)
4. Click "Convert to Speech"
5. Download your MP3 file when ready

### File Upload Mode
1. Click on the "File Upload" tab
2. Select a .txt file (maximum 16MB)
3. Choose your preferred tone
4. Click "Upload & Convert"
5. Download your MP3 file when ready

## Technical Details

- **Backend**: Flask (Python)
- **Text-to-Speech**: Google Text-to-Speech (gTTS)
- **Frontend**: HTML5, CSS3, JavaScript
- **File Handling**: Secure file upload with validation
- **Audio Format**: MP3

## File Structure

```
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Main web interface
├── uploads/           # Generated audio files (created automatically)
└── README.md          # This file
```

## Supported Languages

The application currently supports English by default, but the gTTS library supports multiple languages. You can modify the `language` parameter in the `text_to_speech` function to support other languages.

## Security Features

- File type validation (.txt only)
- File size limits (16MB maximum)
- Secure filename handling
- Automatic file cleanup
- Input sanitization

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Troubleshooting

### Common Issues

1. **"No module named 'flask'" error:**
   - Make sure you've installed the requirements: `pip install -r requirements.txt`

2. **Audio conversion fails:**
   - Check your internet connection (gTTS requires internet)
   - Ensure the text is not empty
   - Try with shorter text first

3. **File upload issues:**
   - Ensure the file is a .txt format
   - Check that the file size is under 16MB
   - Verify the file contains readable text

### Performance Tips

- For large text files, consider breaking them into smaller chunks
- The application automatically cleans up generated files after download
- Generated files are stored temporarily and removed after 5 seconds

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this application. 