#tourism_django
Small site about tourism written on Django web framework. You can adapt it to your own purposes.
 
 
## Quick install
```
Step 1: 
$ git clone https://github.com/artempy/tourism_django .
```
 
Step 2: 
Create a ```src/tourism/settings/.env``` file:
```
DATABASE_NAME=db_name
DATABASE_USER=db_user
DATABASE_PASSWORD=db_password
SECRET_KEY=your_secret_key
EMAIL_HOST=smtp.yandex.ru
EMAIL_HOST_USER=email@yandex.ru
EMAIL_HOST_PASSWORD=email_pasword
EMAIL_PORT=587
EMAIL_USE_TLS=True
FEEDBACK_EMAIL=email@yandex.ru
FROM_EMAIL=email@yandex.ru
```
 
```
Step 3:
$ docker-compose up --build -d
```

Step 4: Go to http://127.0.0.1
