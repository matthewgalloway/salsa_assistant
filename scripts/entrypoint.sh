#!/bin/sh


set -e

python manage.py collectstatic --noinput
python manage.py wait_for_db
python manage.py migrate

uwsgi --socker :9000 --worker 4 --master --enable-threads --module app.wsgi