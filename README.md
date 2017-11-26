## Web-application crawler

Web crawler for [Fendi](https://www.fendi.com)

## Install
``` bash
$ python3 -m venv env_name
$ . env_name/bin/activate
$ pip install -r requirements.txt
```
## PostgreSQL
``` bash
    $ sudo apt-get install postgresql postgresql-server-dev-9.5
```
open postgres console:
``` bash
    $ sudo -u postgres psql postgres
```
create administrator with password and create new user and database for the project:
``` bash
    $ create user pasha with password 123;
    $ create database django_scrapy_fendi owner pasha;
    $ \q
```
Finally do migrations:
``` bash
    $ python manage.py makemigrations
    $ python manage.py migrate
```
then create superuser for the project:
``` bash
    $ python manage.py createsuperuser
```
and run:
``` bash
    $ python manage.py runserver
```
