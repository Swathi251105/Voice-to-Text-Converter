from flask import Flask, render_template, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=8)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language="en")
        return jsonify({'text': text})
    except sr.UnknownValueError:
        return jsonify({'error': "Could not understand audio"})
    except sr.RequestError:
        return jsonify({'error': "API unavailable"})

if __name__ == '__main__':
    app.run(debug=True)
