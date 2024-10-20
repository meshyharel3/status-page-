# Use the official Python image from the Docker Hub
FROM python:3.12

RUN mkdir -p /opt/status-page

# Set the working directory
WORKDIR .

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose the port that the app runs on
EXPOSE 8001

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

