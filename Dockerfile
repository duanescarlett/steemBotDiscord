# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install discord
RUN pip install -U discord.py

RUN pip install -r requirements.txt


# Run app.py when the container launches
CMD ["python", "core.py"]
