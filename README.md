# ASSR - Automatic Speech Sentiment Recognition
###### speech to text and sentiment analysis Webapp
###### CSAI308 - Introduction to Natural Language Processing / college project / March 2024.

This web application has the ability to convert speech to text and perform sentiment analysis on the transcribed text. This is achieved through the use of Google Cloud's Speech-to-Text and Natural Language APIs.

The speech-to-text conversion is handled by the OpenAI client in the home function in app.py. When a user uploads an audio file, the OpenAI client transcribes the audio into text. This transcription is multilingual because Google's Speech-to-Text API supports multiple languages.

The sentiment analysis is performed by the sample_analyze_sentiment function in app.py. This function takes the transcribed text as input and uses the LanguageServiceClient from Google Cloud's Natural Language API to analyze the sentiment of the text. The sentiment analysis is also multilingual, as Google's Natural Language API supports multiple languages.

The results of the transcription and sentiment analysis are then displayed on the web page, as seen in the code from templates/index.html. The transcribed text is displayed under "Transcription", and the sentiment analysis results are displayed under "Sentiment Analysis". The sentiment analysis results include the overall sentiment score and magnitude of the document, as well as the sentiment score and magnitude of each sentence in the document. The language of the text is also displayed.

**Note:** This application can be deployed on the internet, allowing users to access it from anywhere.

## Getting Started

To get started with ASSR, follow these steps:

1. Clone the repository and change current directory:
    ```
    git clone https://github.com/M1419/ASSR.git
    
    cd ASSR
    ```

2. Create an env directory and place a `.env` file in the root of the project then add your OpenAI API key and google application credentials inside it:
    # bash (unix) # replace "your_api_key_here" and application_default_credentials.json file name with your own!
    ```
    echo "OPENAI_API_KEY=your_api_key_here" > .env
    echo "GOOGLE_APPLICATION_CREDENTIALS=\"./application_default_credentials.json\"" >> .env
    ```
    # powershell (windows) # replace "your_api_key_here" and application_default_credentials.json file name with your own!
    ```
    "`nOPENAI_API_KEY=your_api_key_here" | Out-File -Append -Encoding utf8 .env
    "`nGOOGLE_APPLICATION_CREDENTIALS=`"./application_default_credentials.json`"" | Out-File -Append -Encoding utf8 .env
    ```

    when running this command
    ```
    cat .env
    ```

    # you should get the following output:
    OPENAI_API_KEY=your_api_key_here
    GOOGLE_APPLICATION_CREDENTIALS="./application_default_credentials.json"

3. place the application_default_credentials.json file inside ASSR/env directory

    ```
    for details see: https://cloud.google.com/docs/authentication/application-default-credentials
    ```

4. Change current directory to root of ASSR and Create and activate a virtual environment:

    # bash (unix):
    ```
    cd ..
    python -m venv myenv
    source myenv/bin/activate
    ```

    # powershell (windows):
    ```
    cd ..
    python -m venv myenv
    . .\myenv\Scripts\Activate
    ```

5. Install the required dependencies in the `requirements.txt` file:
    ```
    pip install -r requirements.txt
    ```

5. Run the ASSR application by executing the main script.
    ```
    python app.py
    ```

6. Run the ASSR application by executing the main script.
    ```
    go to http://localhost:8080 in your browser
    ```

## License

This project is licensed under the [MIT License](LICENSE).