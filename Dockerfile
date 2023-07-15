# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

FROM python:latest

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV PORT 5000
# Expose the port that the application listens on.
EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]



# Run the application.


