FROM python:3.10-slim

# Install Tesseract and fonts for multilingual support
RUN apt-get update && \
    apt-get install -y tesseract-ocr \
    tesseract-ocr-hin tesseract-ocr-jpn tesseract-ocr-eng \
    libtesseract-dev libleptonica-dev \
    fonts-noto fonts-noto-cjk && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default command
CMD ["python", "main.py"]
