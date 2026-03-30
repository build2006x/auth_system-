# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /auth_system-

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project
COPY . .

# Expose FastAPI's default port
EXPOSE 8000

# Run with uvicorn (FastAPI's server)
CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "8000"]