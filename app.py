import logging
from flask import Flask, request, render_template, send_from_directory
from waitress import serve
from openai import OpenAI
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import platform
import json

app = Flask(__name__)

# Load environment variables
load_dotenv('.env')
# Get the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OpenAI API key found in environment variables")

def sample_analyze_sentiment(text_content):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": """You are a sophisticated sentiment analysis tool. Analyze the given text and provide a detailed sentiment analysis including:
            1. Overall sentiment score (-1.0 to 1.0, where -1 is very negative, 0 is neutral, and 1 is very positive)
            2. Sentiment magnitude (0.0 to +inf, indicating the strength of emotion)
            3. Dominant emotions detected (e.g., joy, anger, sadness, fear, surprise)
            4. Key phrases or words that influenced the sentiment
            5. A brief explanation of the sentiment analysis
            
            Provide your response in the following format:
            Overall sentiment score: [score]
            Sentiment magnitude: [magnitude]
            Dominant emotions: [emotion1, emotion2, ...]
            Key phrases: [phrase1, phrase2, ...]
            Explanation: [Your explanation here]"""},
            {"role": "user", "content": f"Analyze the sentiment of the following text:\n\n{text_content}"}
        ],
        max_tokens=500
    )
    
    sentiment_analysis = response.choices[0].message.content.strip()
    
    # Parse the response
    lines = sentiment_analysis.split('\n')
    sentiment_data = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            sentiment_data[key.strip().lower().replace(' ', '_')] = value.strip()
    
    # Create a response that only includes non-empty fields
    response_data = {
        "document_sentiment": {
            "score": float(sentiment_data.get("overall_sentiment_score", 0)),
            "magnitude": float(sentiment_data.get("sentiment_magnitude", 0))
        },
        "dominant_emotions": [e.strip() for e in sentiment_data.get("dominant_emotions", "").strip("[]").split(',') if e.strip()],
        "key_phrases": [p.strip() for p in sentiment_data.get("key_phrases", "").strip("[]").split(',') if p.strip()],
        "explanation": sentiment_data.get("explanation", ""),
        "language_code": "en"
    }
    
    return response_data

@app.route('/', methods=['GET', 'POST'])
def home():
    transcript = None
    filename = None
    sentiment_data = None
    if request.method == 'POST':
        if 'form02-whats-on-your-mind' in request.form and request.form['form02-whats-on-your-mind']:
            transcript = request.form['form02-whats-on-your-mind']
            sentiment_data = sample_analyze_sentiment(transcript)
        elif 'form02-upload-audio-instead' in request.files:
            file = request.files['form02-upload-audio-instead']
            if file.filename == '':
                return 'No selected file', 400
            if file:
                filename = secure_filename(file.filename)
                # Check the operating system
                if platform.system() == 'Windows':
                    # Save the file in the current directory for Windows
                    filepath = os.path.join(os.getcwd(), filename)
                else:
                    # Save the file in the /tmp directory for other operating systems
                    filepath = os.path.join('/tmp', filename)
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
                finally:
                    # Delete the file after processing
                    if os.path.exists(filepath):
                        os.remove(filepath)
    return render_template('index.html', transcript=transcript, audio_file=filename, sentiment_data=sentiment_data)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    serve(app, host="0.0.0.0", port=8080)
