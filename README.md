# ASSR - Automatic Speech Sentiment Recognition
###### speech to text and sentiment analysis Webapp
###### CSAI308 - Introduction to Natural Language Processing / college project / March 2024.

**Overview**
This web application leverages advanced technologies to provide speech-to-text conversion and comprehensive sentiment analysis. Core functions include:

**Technical Foundation**
* **Open AI Whisper:**  Employed for robust multilingual speech-to-text capabilities.
* **Google Cloud Natural Language API:** Provides sophisticated sentiment analysis with multilingual compatibility.

**Value Proposition**
ASSR has potential applications in various fields:
* **Customer Service:** Analyze call transcripts to gauge customer satisfaction and identify areas for improvement.
* **Market Research:**  Assess sentiment towards products or brands through recorded interviews and focus groups.
* **Accessibility:** Assist individuals with hearing impairments by providing transcriptions enhanced with emotional context.

**Project Status**
This project, developed for a Natural Language Processing course, demonstrates the power of combining AI technologies for nuanced language understanding.
**Note:** This application can be deployed on the internet, allowing users to access it from anywhere.

## Screenshots

![Screenshot 1](https://raw.githubusercontent.com/M1419/misc/main/h/en-neg-example.png)
![Screenshot 2](https://raw.githubusercontent.com/M1419/misc/main/h/ar-pos-example.png)

# Getting Started

Follow these steps to get started with ASSR:

1. Clone the repository and change current directory:

    ```sh
    git clone https://github.com/vwkyc/ASSR.git
    cd ASSR
    ```

2. Place a `.env` file in the root of the project. Add your OpenAI API key and Google application credentials inside it:

    Unix-like:
    ```sh
    echo "OPENAI_API_KEY=your_api_key_here" > .env
    echo "GOOGLE_APPLICATION_CREDENTIALS=\"./application_default_credentials.json\"" >> .env
    ```

    PowerShell:
    ```powershell
    "OPENAI_API_KEY=your_api_key_here" | Out-File -FilePath .env -Encoding ascii
    "GOOGLE_APPLICATION_CREDENTIALS=\"./application_default_credentials.json\"" | Add-Content .env
    ```

    Verify the contents of the `.env` file:

    Unix-like:
    ```sh
    cat .env
    ```

    PowerShell:
    ```powershell
    Get-Content .env
    ```

3. Place the `application_default_credentials.json` file in the root directory. For details, see [Google Cloud's documentation](https://cloud.google.com/docs/authentication/application-default-credentials).

4. Change current directory to root of ASSR and create and activate a virtual environment:

    Unix-like:
    ```sh
    python -m venv myenv
    source myenv/bin/activate
    ```

    PowerShell:
    ```powershell
    py -m venv myenv
    .\myenv\Scripts\Activate
    ```

5. Install the required dependencies from the `requirements.txt` file:

    Unix-like:
    ```sh
    pip install -r requirements.txt
    ```

    PowerShell:
    ```powershell
    pip install -r .\requirements.txt
    ```

6. Run the ASSR application:

    ```sh
    python app.py
    ```

7. Open the application in your browser at [http://localhost:8080](http://localhost:8080).
