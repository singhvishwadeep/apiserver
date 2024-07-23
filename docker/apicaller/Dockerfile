# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /usr/local/bin/

# Install Python
RUN apt-get update
RUN apt install -y curl dnsutils

# Copy the current directory contents into the container at /usr/src/app
COPY scripts/run.sh .

# Run app.py when the container launches
CMD ["sh", "run.sh"]
