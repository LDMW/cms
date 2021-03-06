#!/bin/bash

cd /home/docker/code/

python manage.py migrate --noinput

# python manage.py collectstatic -c --no-input --settings cms.settings.production
python manage.py collectstatic -c --no-input --settings $DJANGO_SETTINGS_MODULE

# python manage.py runserver --settings cms.settings.production 127.0.0.1:8001
/usr/local/bin/uwsgi --ini /home/docker/code/uwsgi.ini
