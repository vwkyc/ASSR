# ASSR - Automatic Speech Sentiment Recognition
###### speech to text and setmient analysis Webapp
###### CSAI308 - Introduction to Natural Language Processing / college project.
###### March 2024

## Getting Started

To get started with ASSR, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/M1419/ASSR.git
    ```

2. Create a `.env` file in the root of the project then add your OpenAI API key and google application credentials inside it:
    ```
    OPENAI_API_KEY=your_api_key_here
    GOOGLE_APPLICATION_CREDENTIALS="application_default_credentials.json"
    ```

3. Create and activate a virtual environment:
    ```
    python -m venv myenv
    source myenv/bin/activate
    ```

4. Install the required dependencies. You can find the list of dependencies in the `requirements.txt` file. Run the following command:
    ```
    pip install -r requirements.txt
    ```

5. Run the ASSR application by executing the main script.
    ```
    python app.py
    ```

## License

This project is licensed under the [MIT License](LICENSE).