FROM python:3.10-slim

# Create app directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

# Use a non-root user for better security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

# Expose port and run with a production server
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "src.app:app", "--workers", "2"]
