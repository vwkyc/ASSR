import logging
from flask import Flask, request, render_template, send_from_directory
from waitress import serve
from openai import OpenAI
import os
import dotenv
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load environment variables
dotenv.load_dotenv()
# Get the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OpenAI API key found in environment variables")

@app.route('/', methods=['GET', 'POST'])
def home():
    transcript = None
    filename = None  # Initialize filename to None
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part in the request', 400
        file = request.files['file']
        if file.filename == '':
            return 'No selected file', 400
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.root_path, 'static', filename)
            file.save(filepath)
            try:
                client = OpenAI(api_key=api_key)
                transcript = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=open(filepath, "rb"),
                    response_format="text"
                )
            except Exception as e:
                print(str(e))  # Log the error but don't return it
    return render_template('index.html', transcript=transcript, audio_file=filename)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve(app, host="0.0.0.0", port=8080)