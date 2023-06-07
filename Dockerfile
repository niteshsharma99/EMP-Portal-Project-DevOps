FROM python:3.8.0-slim
COPY . /home/flask-app
WORKDIR /home/flask-app
RUN pip install -r requirements.txt 