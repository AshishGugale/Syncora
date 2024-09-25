# Backend setup

## Setting up the virtual environment and getting deps installed
python3 -m venv vevn
source vevn/bin/activate
pip install -r requirements.txt

## Django migrations
python manage.py makemigrations
python manage.py migrate

## Creating superuser
python manage.py createsuperuser

## Server startup
python manage.py runserver

Access it at - http://127.0.0.1:8000/admin