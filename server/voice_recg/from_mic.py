import speech_recognition as sr

def execute_command(text):
    # Define actions based on keywords
    if "hello" in text:
        print("Greetings!")
    if "bye" in text:
        print("Goodbye!")
    if "macaco louco" in text:
        print("mokeko")
    # Add more commands as needed

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

def listen_for_speech():
    with sr.Microphone() as source:
        # Reduce the recognizer sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for commands...")

        while True:
            try:
                # Listen for the first phrase and extract it into audio data
                audio = recognizer.listen(source, timeout=15, phrase_time_limit=3)
                # Recognize speech using Google Web Speech API
                text = recognizer.recognize_google(audio, language='pt-BR')
                print("You said: {}".format(text))

                # Execute command based on the recognized text
                execute_command(text.lower())

            except sr.WaitTimeoutError:
                # Handle the case where listen times out without receiving audio
                print("Listening timed out, try again...")
            except sr.UnknownValueError:
                # Catch unrecognized speech
                print("Could not understand audio, please try again...")
            except sr.RequestError as e:
                # Catch API errors
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

listen_for_speech()
