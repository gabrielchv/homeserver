import speech_recognition as sr

def execute_command(text):
    commands = []
    # Define actions based on keywords
    if "teste" in text:
        commands.append("teste!")
    if "um" in text:
        commands.append("um!")
    if "dois" in text:
        commands.append("dois!")
    if "macaco louco" in text:
        commands.append("macaco louco!")
    # Add more commands as needed
    return commands

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

def listen_for_speech_from_file(audio_file: sr.AudioFile):

    data = {}

    # Use the audio file as the audio source
    with audio_file as source:
        # Listen for the data (load audio to memory)
        audio_data = recognizer.record(source)
        # Recognize (convert from speech to text)
        try:
            text = recognizer.recognize_google(audio_data, language='pt-BR')
            data["text"] = text

            # Execute command based on the recognized text
            data["commands"] = execute_command(text.lower())

            return data

        except sr.UnknownValueError:
            # Catch unrecognized speech
            print("Could not understand audio")
        except sr.RequestError as e:
            # Catch API errors
            print("Could not request results; {0}".format(e))

# Path to your audio file (update this to the path of your audio file)
audio_file_path = './audio_file.wav'
listen_for_speech_from_file(sr.AudioFile(audio_file_path))