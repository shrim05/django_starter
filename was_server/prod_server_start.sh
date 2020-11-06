#! /bin/bash

python ./manage.py makemigrations
python ./manage.py migrate
echo 'static files collecting'
echo yes | python ./manage.py collectstatic
gunicorn \
    conf.wsgi:application \
    --bind 0.0.0.0:8000 \
    --max-requests 1000 \
    --max-requests-jitter 50