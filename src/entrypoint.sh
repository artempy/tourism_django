#!/bin/bash

cd /www/src

echo "Migrating the database before starting the server."
python manage.py makemigrations --settings=tourism.settings.dev
python manage.py migrate --settings=tourism.settings.dev
python manage.py collectstatic --noinput --settings=tourism.settings.dev

python ./manage.py runserver 0.0.0.0:8000 --settings=tourism.settings.dev
#echo "Starting Gunicorn."
#exec gunicorn --env DJANGO_SETTINGS_MODULE=tourism.settings.prod 'tourism.wsgi:get_wsgi_application()' \
#    --bind 0.0.0.0:8000 \
#    --workers 2
