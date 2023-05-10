# Use the official Python base image
FROM python:3.9-alpine3.13
LABEL maintainer='matthew.galloway19@gamil.com'

# Copy requirements.txt and install dependencies
ENV PYTHONBUFFERED 1
COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
# Set the working directory
WORKDIR /app
# Expose the port the app will run on
EXPOSE 8000


ARG DEV=false
RUN pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    pip install -r /tmp/requirements.txt\
    fi

RUN rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user
ENV PATH="/py/bin:$PATH"

USER django-user









