#!/bin/sh

python manage.py tailwind install --no-input;
python manage.py tailwind build --no-input;
python manage.py collectstatic --no-input;
python manage.py migrate

gunicorn belayme.wsgi --bind :8080 --workers 2 --access-logfile -
