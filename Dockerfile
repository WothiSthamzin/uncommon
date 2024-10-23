# Using the official Python image
FROM python:3.11-slim

# Setting environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Setting the working directory
WORKDIR /app

# Installing dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copying the project files
COPY . /app/

# Exposing the port the app runs on
EXPOSE 8000

# Starting the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
