# Gavilan College Computer Science Club

* currently works on python 3.7.2 and 3.7.3
* make sure to __check the requirements.txt__ for the modules required to work on project
* best practices is to use a python virtual environment for the project E.g virtualenv
* you might need to create a new superuser when cloning repo by running command: `python manage.py createsuperuser` or if that does not work: `winpty python manage.py createsuperuser` __in dir with manage.py__
* make sure to __change the ‘SECRET_KEY’ in the settings file when deploying app__
* makesure to run `python manage.py collectstatic` and __type yes__ so ckedit can work after all req modules installed
* then run command: `python manage.py migrate` so it can update the local development database
* finally run command: `python manage.py runserver` to run the server on __localhost:8000__
* for more info message me, any club chairperson or check Django documentation