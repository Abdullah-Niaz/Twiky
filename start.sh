#!/bin/bash

# Exit if any command fails
set -e

# Collect static files
python3 manage.py collectstatic --noinput

# Run Gunicorn WSGI server
gunicorn Twiky.wsgi:application --bind 0.0.0.0:$PORT
