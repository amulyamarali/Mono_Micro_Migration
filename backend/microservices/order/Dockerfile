# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code to the working directory
COPY . .

# Make port 8000 available to the outside world
EXPOSE 7000

# Define the command to run the app
CMD [ "python", "server.py" ]