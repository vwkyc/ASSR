import logging
from flask import Flask, request, render_template, send_from_directory
from waitress import serve
from openai import OpenAI
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from google.cloud import language_v2

app = Flask(__name__)

# Load environment variables
load_dotenv('env/.env')
# Get the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OpenAI API key found in environment variables")

def sample_analyze_sentiment(text_content):
    client = language_v2.LanguageServiceClient()
    document_type_in_plain_text = language_v2.Document.Type.PLAIN_TEXT
    document = {
        "content": text_content,
        "type_": document_type_in_plain_text,
    }
    encoding_type = language_v2.EncodingType.UTF8
    response = client.analyze_sentiment(
        request={"document": document, "encoding_type": encoding_type}
    )
    return response

@app.route('/', methods=['GET', 'POST'])
def home():
    transcript = None
    filename = None
    sentiment_data = None
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
                sentiment_data = sample_analyze_sentiment(transcript)
            except Exception as e:
                print(str(e))
    return render_template('index.html', transcript=transcript, audio_file=filename, sentiment_data=sentiment_data)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve(app, host="0.0.0.0", port=8080)