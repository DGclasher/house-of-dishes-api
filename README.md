# house-of-dishes-api

### Setup local development server

Create python venv in root dir of project
```
python3 -m venv venv && source venv/bin/activate
```
Migrate
```
python3 manage.py migrate --noinput 
```
Run the server
```
python3 manage.py runserver
```
