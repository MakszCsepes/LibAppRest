FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# install FastAPI with all its dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the local script into the container
COPY main.py .

# Expose port (optional, but informative)
EXPOSE 8000


CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]