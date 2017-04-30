@echo off

python freelancr/manage.py makemigrations users_app
python freelancr/manage.py makemigrations
python freelancr/manage.py migrate
python freelancr/manage.py runserver
