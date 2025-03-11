# Base image for Python 3.12
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy only the requirements file first
COPY requirements.txt .

# Installer les dépendances nécessaires pour pygame
RUN apt-get update && \
    apt-get install -y \
    python3-dev \
    libfreetype6-dev \
    libsdl2-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-ttf-2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libfontconfig1 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Define the command to run when the container starts
CMD ["python", "main.py"]

# Run the Docker image (no gui , too complex)
# docker run -p 4000:80 my-python-app

