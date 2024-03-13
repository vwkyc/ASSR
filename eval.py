# this is to test the WER using a downloaded .tgz dataset from https://www.openslr.org/108/
import pandas as pd
from datasets import Dataset
from transformers import WhisperForConditionalGeneration, WhisperProcessor
import torch
import os
import soundfile as sf
from evaluate import load
import jiwer
# Replace 'env/AR' with the path to your dataset files directory
audio_dir = 'env/AR'

# Get a list of all audio files in the directory
audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.flac')]

# Load the audio files and their transcriptions
data = []
for audio_file in audio_files:
    audio, sr = sf.read(os.path.join(audio_dir, audio_file))
    with open(os.path.join(audio_dir, audio_file.replace('.flac', '.txt')), 'r') as f:
        transcription = f.read().strip()
    data.append({'audio': {'array': audio, 'sampling_rate': sr}, 'text': transcription})

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Convert the DataFrame to a dictionary
data_dict = df.to_dict('list')

# Create a Dataset object
your_dataset = Dataset.from_dict(data_dict)

processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2").to("cuda")

def map_to_pred(batch):
    audio = batch["audio"]
    input_features = processor(audio["array"], sampling_rate=audio["sampling_rate"], return_tensors="pt").input_features.to("cuda")
    batch["reference"] = processor.tokenizer._normalize(batch['text'])

    with torch.no_grad():
        predicted_ids = model.generate(input_features)[0]
    transcription = processor.decode(predicted_ids)
    batch["prediction"] = processor.tokenizer._normalize(transcription)
    return batch

result = your_dataset.map(map_to_pred)

wer = load("wer")
print(100 * wer.compute(references=result["reference"], predictions=result["prediction"]))