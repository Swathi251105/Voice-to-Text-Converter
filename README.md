# Voice-to-Text Converter

## Project Description
This is a web-based Voice-to-Text Converter that allows users to convert spoken words into text using Flask and the Google Speech Recognition API. The simple UI provides real-time transcription, making it useful for note-taking and accessibility. Built with Python, Flask, HTML, CSS, and JavaScript.This project is a web-based Voice-to-Text Converter that allows users to convert their spoken words into text. It is built using Flask for the backend and HTML, CSS, and JavaScript for the frontend. The application utilizes the Google Speech Recognition API to process voice input and display the converted text on the screen. This tool is useful for transcription, note-taking, and accessibility purposes.

## Features
- Real-time speech-to-text conversion
- Simple and interactive UI
- Flask backend with SpeechRecognition
- Works on modern web browsers

## Technologies Used
- **Backend**: Python, Flask, SpeechRecognition
- **Frontend**: HTML, CSS, JavaScript

## GitHub Repository
Project Link: https://github.com/Swathi251105/Voice-to-Text-Converter


## Installation

### 1. Install Python
- Download and install Python from [python.org](https://www.python.org/downloads/).
- Ensure `pip` is installed by running:
  ```bash
  python -m ensurepip --default-pip
  ```

### 2. Install VS Code
- Download and install [VS Code](https://code.visualstudio.com/).
- Install the **Python extension** in VS Code.

### 3. Set Up Virtual Environment
- Open a terminal in VS Code (`Ctrl + ~`).
- Create a virtual environment:
  ```bash
  python -m venv venv
  ```
- Activate the virtual environment:
  - On Windows:
    ```bash
    venv\Scripts\activate
    ```
  - On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

### 4. Install Dependencies
  ```bash
  pip install flask SpeechRecognition
  ```

### 5. Run the Flask App
  ```bash
  python app.py
  ```

### 6. Open in Browser
  ```
  http://127.0.0.1:5000/
  ```

## Project Structure
```
voice-to-text/
│-- app.py          # Flask backend
│-- templates/
│   ├── index.html  # Frontend HTML
│-- static/
│   ├── style.css   # Stylesheet (if used separately)
```

## Usage
- Click the microphone button
- Speak into your microphone
- The recognized text will be displayed on the screen

## License
This project is licensed under the MIT License.

## Acknowledgments
- Google Speech Recognition API
- Flask framework


