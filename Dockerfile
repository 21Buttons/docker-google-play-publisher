FROM python:3.7-slim

RUN pip install --no-cache-dir google-api-python-client oauth2client pyOpenSSL

COPY upload_bundle_to_alpha.py /upload_bundle_to_alpha.py

CMD ["python", "upload_bundle_to_alpha.py"]
