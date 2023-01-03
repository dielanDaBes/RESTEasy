FROM arm32v6/python:3.9-alpine


COPY restEasy.py ./
COPY requirements.txt requirements.txt
ADD ./static /static

# Intall the required modules
RUN pip install -r requirements.txt

# Trigger Python script
CMD ["python", "./restEasy.py"]
