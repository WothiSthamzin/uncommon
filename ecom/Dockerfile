# Using the official Python image
FROM python:3.9-slim

# Setting the working directory
WORKDIR /app

# Copying requirements
COPY requirements.txt .

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying the entire Django App into container
COPY . .

# Exposing the port the app runs on
EXPOSE 8000

# Starting the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
