# Using python official image as the base image
FROM python:3.8.0-slim

# Set the working directory inside the container
WORKDIR /home/flask-app

#Copy the application code to Container.
COPY . /home/flask-app

# Install the required dependencies to run application
RUN pip install -r requirements.txt

# Setting required environment variable for the application and database.
ENV DATABASE="emp_db.db"
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Creation of database tables
CMD flask db upgrade

# Command to execute whenever the container starts
ENTRYPOINT flask run


