FROM python:3.7-alpine

RUN pip install --no-cache-dir google-api-python-client oauth2client

COPY upload_bundle_to_alpha.py /upload_bundle_to_alpha.py
COPY docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
