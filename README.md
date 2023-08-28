# House of Dishes API

### Setup local development server
Create a `.env` file at the root directory of project, refer to [this](./.env.example) for `.env` file. 
For `SECRET_KEY`, get one from [here](https://djecrety.ir/).
For Google auth keys, get your keys from [here](https://console.cloud.google.com/apis/credentials).
#### For Linux Users
Create python venv in root dir of project
```
python3 -m venv venv && source venv/bin/activate
```
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
#### Same for both
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