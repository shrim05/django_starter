#! /bin/bash

# django dev mode start
echo 'make migration start'
python ./manage.py makemigrations
echo 'migration start'
python ./manage.py migrate
echo 'runserver 0:8000'
python ./manage.py runserver 0:8000