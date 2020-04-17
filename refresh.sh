#! /bin/bash

rm -rf db.sqlite3 quality/migrations/000*

python manage.py makemigrations

cp quality/init_migrations/* quality/migrations/

python manage.py migrate

python manage.py createsuperuser --email admin@admin.com --username=admin

python manage.py runserver
