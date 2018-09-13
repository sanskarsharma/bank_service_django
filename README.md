# Bank Finder app

This is a webapp for finding bank branches in a city or looking up bank branches details by IFSC code.
It is live on : https://damp-brushlands-95623.herokuapp.com

## About project
- made upon python Django-REST framework.
- Database used is PostgreSQL, managed by django ORM.
- Bootstrap4 with jQuery on the frontend.

All APIs follow REST spec and are called from frontend via AJAX requests.

## Prerequisites for setup
- Python3 with virtualenv

- PostgreSQL server, local/remote


## Build / Run 
-> git pull/clone

-> create and activate a python virtualenv

-> Install requirements insite virtualenv : `$ pip install -r requirements.txt`

-> Create an empty database on local psql 

-> Import the dump sql file [indian_banks.sql](https://github.com/snarayanank2/indian_banks) to the created database

-> Add all database credentials/settings to settings.py file

-> Run migrations on django to make necessary db tables : `python manage.py migrate`

-> Run app : `python manage.py runserver`

-> app will be live on `localhost:8000`


#### Developer contact
 - [ github ](https://github.com/sanskarsharma)
 - [ linkedin ](https://linkedin.com/in/sanskarssh)
 - [angel](https://angel.co/sanskarsharma)

     
