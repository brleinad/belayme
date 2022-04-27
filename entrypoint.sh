#!/bin/sh

python manage.py tailwind install --no-input;
python manage.py tailwind build --no-input;
python manage.py collectstatic --no-input;
python manage.py migrate

gunicorn belayme.wsgi -b 0.0.0.0:8000 --access-logfile -
