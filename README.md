# house-of-dishes-api

### Setup local development server

Create python venv in root dir of project
```
python -m venv venv && source venv/bin/activate
```
Create a `.env` file at the root directory of project, refer to [this](./.env.example) for `.env` file. 
Migrate
```
python manage.py migrate --noinput 
```
Run the server
```
python manage.py runserver
```
