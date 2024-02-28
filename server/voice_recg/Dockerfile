# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install input/output dependencies
RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 flac portaudio19-dev -y

# Install Python dependencies
RUN pip install --no-cache-dir flask PyAudio SpeechRecognition

EXPOSE 5000

# Your application's default command
CMD ["python", "-u", "./server.py", "--host=0.0.0.0:5000"]
