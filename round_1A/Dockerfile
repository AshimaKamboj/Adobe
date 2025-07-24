# FROM python:3.10-slim

# # Set working directory
# WORKDIR /app

# # Install system dependencies for OCR and multilingual support
# RUN apt-get update && \
#     apt-get install -y \
#         tesseract-ocr \
#         tesseract-ocr-eng \
#         tesseract-ocr-hin \
#         tesseract-ocr-jpn \
#         libtesseract-dev \
#         libleptonica-dev \
#         poppler-utils \
#         fonts-noto \
#         fonts-noto-cjk \
#         libglib2.0-0 \
#         libsm6 \
#         libxext6 \
#         libxrender-dev && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# # Copy application code into container
# COPY . .

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Set default command
# CMD ["python", "main.py"]

FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for OCR, multilingual support, and Ghostscript
RUN apt-get update && \
    apt-get install -y \
        tesseract-ocr \
        tesseract-ocr-eng \
        tesseract-ocr-hin \
        tesseract-ocr-jpn \
        libtesseract-dev \
        libleptonica-dev \
        poppler-utils \
        ghostscript \
        fonts-noto \
        fonts-noto-cjk \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy app files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default command
CMD ["python", "main.py"]
