# Use the official Python image from the Docker Hub
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# The default command is to start the Django development server
CMD ["gunicorn", "conf.wsgi:application", "--bind", "0.0.0.0:8000"]