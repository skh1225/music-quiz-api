#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 2 --master --enable-threads --module app.wsgi
daphne -b 0.0.0.0 -p 8001 app.asgi:application