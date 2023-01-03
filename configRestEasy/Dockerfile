# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v6/python:3.9-alpine

# Copy the Python Script to blink LED
COPY configureRestEasy.py ./
COPY requirements.txt requirements.txt
ADD ./templates /templates
ADD ./static /static
ENV FLASK_APP=configureRestEasy

# Intall the required modules
RUN pip install -r requirements.txt

# Trigger Python script
CMD ["python", "./configureRestEasy.py"]
