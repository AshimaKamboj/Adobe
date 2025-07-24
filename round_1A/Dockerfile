# FROM --platform=linux/amd64 python:3.10-slim

# WORKDIR /app

# COPY . .

# RUN pip install --no-cache-dir -r requirements.txt

# ENTRYPOINT ["python", "main.py"]
# Use official Python image
FROM python:3.10-slim

# Create working directory
WORKDIR /app

# Install fonts for multilingual support (e.g., Japanese, Hindi)
RUN apt-get update && \
    apt-get install -y fonts-noto fonts-noto-cjk && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run script on container start
CMD ["python", "main.py"]
