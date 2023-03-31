FROM python:3.11.2-alpine

# OS and Python Starting Package install/patching
RUN apk update && apk upgrade
RUN apk add --no-cache build-base gcc make tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install --upgrade pip && pip install --upgrade wheel setuptools

# Create folder structure for image to use.
RUN mkdir -p /app /certs /logs
RUN chmod -R 770 /app /certs /logs
WORKDIR /app

# Copy application into created folder structure.
COPY ./src /app

# Install application dependencies from file.
RUN pip install -r /app/requirements.txt

# Run app as user
USER 1001

# Command to start app split by space
CMD ["python3", "-B", "/app/main.py"]