import speech_recognition as sr
from flask import Flask, request, jsonify
from from_file import listen_for_speech_from_file

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    # check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']

    data = listen_for_speech_from_file(sr.AudioFile(file))

    print("\033[92m" + "value: " + "\033[96m", data, "\033[0m")

    return jsonify({'data': data}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
