from flask import Flask, request, render_template
from openai import OpenAI
import os
import dotenv
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load environment variables
dotenv.load_dotenv()
client = OpenAI()
# Get the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OpenAI API key found in environment variables")

@app.route('/', methods=['GET', 'POST'])
def home():
    transcript = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part in the request', 400
        file = request.files['file']
        if file.filename == '':
            return 'No selected file', 400
        if file:
            filename = secure_filename(file.filename)
            file.save(filename)
            audio_file = open(filename, "rb")
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file,
                response_format="text"
            )
    return render_template('index.html', transcript=transcript)

if __name__ == '__main__':
    app.run(debug=True, port=8000)