# Starts from the python 3.10 official docker image
FROM python:3.10-slim-bullseye

# Create a folder "app" at the root of the image
RUN mkdir /app

# Define /app as the working directory
WORKDIR /app

# Copy all the files in the current directory in /app
COPY . /app

# Update pip
RUN pip install --upgrade pip

# Install dependencies from "requirements.txt"
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the app
ENTRYPOINT ["python3", "app.py"]
