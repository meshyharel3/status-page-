# Use the official Python image from the Docker Hub
FROM python:3.12

RUN mkdir -p /opt/status-page

# Set the working directory
WORKDIR /opt/status-page

# Copy the entire project
COPY . .
RUN bash upgrade.sh

# Expose the port that the app runs on
EXPOSE 8001

CMD ["/opt/status-page/venv/bin/gunicorn", "--pid" ,"/var/tmp/status-page.pid" ,"--pythonpath" ,"/opt/status-page/statuspage" ,"--config" ,"/opt/status-page/gunicorn.py", "statuspage.wsgi"]

