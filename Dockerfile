FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# install FastAPI
RUN pip install fastapi uvicorn

# Copy the local script into the container
COPY main.py .

# Expose port (optional, but informative)
EXPOSE 8000


CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]