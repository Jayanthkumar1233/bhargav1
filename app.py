from flask import Flask, request, render_template, jsonify, send_file, flash
from werkzeug.utils import secure_filename
import os
import tempfile
from gtts import gTTS
import uuid
import re

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_file(file_path):
    """Extract text from uploaded file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # Try with different encoding if UTF-8 fails
        with open(file_path, 'r', encoding='latin-1') as file:
            return file.read()

def text_to_speech(text, tone='neutral', language='en'):
    """Convert text to speech with specified tone"""
    
    # Clean and prepare text
    text = re.sub(r'\s+', ' ', text.strip())
    if not text:
        return None, "No text content found"
    
    # Tone-specific text modifications
    if tone == 'suspenseful':
        # Add dramatic pauses and slower speech
        text = text.replace('.', '...').replace('!', '...!')
        slow = True
    elif tone == 'inspiring':
        # Add emphasis and clearer pronunciation
        text = text.replace('.', '!').replace('!', '!!')
        slow = False
    else:  # neutral
        slow = False
    
    try:
        # Generate unique filename
        filename = f"speech_{uuid.uuid4().hex}.mp3"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Create gTTS object with tone-specific settings
        tts = gTTS(text=text, lang=language, slow=slow)
        tts.save(filepath)
        
        return filepath, None
    except Exception as e:
        return None, str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text():
    try:
        text_input = request.form.get('text', '').strip()
        tone = request.form.get('tone', 'neutral')
        language = request.form.get('language', 'en')
        
        # Check if text was provided
        if not text_input:
            return jsonify({'error': 'Please provide some text to convert'}), 400
        
        # Validate tone
        valid_tones = ['neutral', 'suspenseful', 'inspiring']
        if tone not in valid_tones:
            tone = 'neutral'
        
        # Convert text to speech
        filepath, error = text_to_speech(text_input, tone, language)
        
        if error:
            return jsonify({'error': error}), 500
        
        # Return success response with file info
        filename = os.path.basename(filepath)
        return jsonify({
            'success': True,
            'filename': filename,
            'message': f'Text converted to {tone} tone successfully!'
        })
        
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Check if file was uploaded
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Only .txt files are allowed'}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extract text from file
        text_content = extract_text_from_file(filepath)
        
        # Clean up uploaded file
        os.remove(filepath)
        
        if not text_content.strip():
            return jsonify({'error': 'The uploaded file is empty or contains no readable text'}), 400
        
        # Get tone and language from form
        tone = request.form.get('tone', 'neutral')
        language = request.form.get('language', 'en')
        
        # Convert text to speech
        audio_filepath, error = text_to_speech(text_content, tone, language)
        
        if error:
            return jsonify({'error': error}), 500
        
        # Return success response
        audio_filename = os.path.basename(audio_filepath)
        return jsonify({
            'success': True,
            'filename': audio_filename,
            'message': f'File converted to {tone} tone successfully!'
        })
        
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/download/<filename>')
def download_file(filename):
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True, download_name=f"speech_{filename}")
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Download error: {str(e)}'}), 500

@app.route('/cleanup/<filename>')
def cleanup_file(filename):
    """Clean up generated audio files"""
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            return jsonify({'success': True, 'message': 'File cleaned up successfully'})
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Cleanup error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 