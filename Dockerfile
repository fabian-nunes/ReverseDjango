FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /reverse_django

# Set the working directory
WORKDIR /reverse_django

# Copy the current directory contents into the container
ADD . /reverse_django/

# Install any needed packages specified in requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy a restricted shell script
COPY limitedshell.sh /usr/local/bin/limitedshell.sh
RUN chmod +x /usr/local/bin/limitedshell.sh

# Set the entrypoint to the restricted shell
ENTRYPOINT ["/usr/local/bin/limitedshell.sh"]