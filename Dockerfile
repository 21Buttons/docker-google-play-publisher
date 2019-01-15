FROM python:3.7-alpine

RUN pip install --no-cache-dir google-api-python-client oauth2client
