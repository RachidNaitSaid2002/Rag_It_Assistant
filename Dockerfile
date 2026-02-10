FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ANONYMIZED_TELEMETRY=False

# Set work directory
WORKDIR /app

COPY ml/Models/ /app/ml/Models/

# ONLY install what is absolutely necessary (usually nothing if using pure python or wheels)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#    curl \
#    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .

RUN ls -la

# --no-cache-dir keeps the image small
#RUN pip install --no-cache-dir -r requirements.txt
# Increase default timeout to 1000 seconds (approx 16 minutes)
RUN pip install --upgrade pip
RUN pip install --no-cache-dir \
  --index-url https://download.pytorch.org/whl/cpu \
  torch==2.1.2+cpu
RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]