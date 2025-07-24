FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies for Tesseract, fonts, and image processing
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    poppler-utils \
    fonts-noto \
    fonts-noto-cjk \
    libjpeg-dev \
    zlib1g-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Command (if needed for local test, override during docker run)
CMD ["python", "main.py"]
