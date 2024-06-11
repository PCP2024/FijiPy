FROM python:3.10-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Create and move to working directory
WORKDIR /app

# Copy the codes 
COPy . /app

# Install pip requirements
#COPY requirements.txt .
RUN python -m pip install -r requirements.txt

#RUN apt-get update && apt-get install libgl1 -y
RUN apt-get update && apt-get install -y python3-opencv \ 
    sudo \ 
	wget \ 
    vim 

ENTRYPOINT ["python", "run_main.py"]
