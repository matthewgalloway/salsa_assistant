# Use the official Python base image
FROM python:3.9-alpine3.13
LABEL maintainer='matthew.galloway19@gamil.com'

# Set environment variables
ENV PYTHONBUFFERED 1
ENV PATH="/scripts:${PATH}"

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk update && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev && \
    pip install --upgrade pip && \
    pip install -r /requirements.txt && \
    apk del .tmp-build-deps && \
    rm -rf /var/cache/apk/*

# Copy the Django application
COPY ./app /app
COPY ./scripts /scripts/
RUN chmod +x /scripts/*

# Add user for application to run as
RUN adduser --disabled-password --no-create-home django-user

USER django-user
VOLUME /vol/web
# Expose the port the app will run on
EXPOSE 8000

CMD ["entrypoint.sh"]
