# Test SOAP Client

Client SOAP Web Service with python 3

Django 2 an zeep

# Install and run

virtualenv env
source env/bin/activate

pip3 install -r requirements.txt

python3 manage.py migrate

python3 manage.py createsuperuser --email [email] --username [usernama]

python3 manage.py runserver

change WSDL_URL and WSDL_CALC_URL vars on settings.py for url of service

start web service [view down]

open browser

localhost:8000/series/list

# Test SOAP Web Service

https://github.com/carlosturnerbenites/soap-service-test
