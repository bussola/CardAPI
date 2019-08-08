#!/bin/bash

python /app/manage.py makemigrations
python /app/manage.py migrate
python /app/manage.py loaddata clients
python /app/manage.py loaddata cards
python /app/manage.py runserver 0.0.0.0:8000
