# Pull the Python Docker image
docker pull python 

# Build the Docker image
docker build -t python-docker-demo .

# Run the Docker container
docker run -p 5000:5000 python-docker-demo
