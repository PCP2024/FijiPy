FROM python:3.10-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Create and move to working directory
WORKDIR /app

# Copy the codes 
COPy . /app

#RUN apt-get update && apt-get install libgl1 -y
RUN apt-get update && apt-get install -y python3-opencv \ 
    sudo \ 
	wget \ 
    vim 

# Install pip requirements
#COPY requirements.txt .
RUN python -m pip install -r requirements.txt

#CMD ["python", "run_main.py"]
# you need ENTRYPOINT to run the code with arguments
ENTRYPOINT ["python", "run_main.py"] 
