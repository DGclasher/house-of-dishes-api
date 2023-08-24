# House of Dishes API

### Setup local development server
Create a `.env` file at the root directory of project, refer to [this](./.env.example) for `.env` file. 
#### For Linux Users
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
---
#### For Windows users
Install `virtualenv`
```
pip install virtualenv
```
Create virtual environment
```
virtualenv venv
```
Activate the environment
```
.\venv\Scripts\activate
```
Install dependencies
```
pip install -r requirements.txt
```
Migrate db
```
python manage.py migrate --noinput
```
Run the server
```
python manage.py runserver
```
---