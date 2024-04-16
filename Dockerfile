# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and JSON file into the container
COPY Script.py .
COPY sqlite.py .
COPY extracted_data.json .

# Install dependencies
RUN pip install requests beautifulsoup4 cloudscraper

# Run the Python script when the container launches
CMD ["python", "Script.py"]
