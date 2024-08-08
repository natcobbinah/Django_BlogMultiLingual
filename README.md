# MULTILINGUAL DJANGO BLOG SITE
A simple django blog site with multilingual features and a chatbot using LLM for processing suitable response to users.

## Features 
```
>   Multilanguage support; supported currently (french and english)

>   Chat-gpt integration, for chat-bot functionality support using 
    Websocket consumers and appropriate routing, with an implemented
    Websocket client

>   Pagination support for viewing list of posts currently available

>   CRUD functionality support for posts

>   Search functionality for posts using its attributes

*   Uses channels to serve project through Asynchronous Server Gateway Interface (ASGI)
```

## Hosted app on heroku (have deleted postgresDB INSTANCE bcos of recurring cost, so run the app locally and test out features
> https://multisite-django-app-d49cbac60017.herokuapp.com/en/

> https://multisite-django-app-d49cbac60017.herokuapp.com/en/admin
> login to admin dashboard, so user instance becomes available for creating and editing posts,
  else only (viewing of posts, chatbot and search functionalities) operations can be performed

> username: <contact me via email at natcobbinah1778@gmail.com for admin dashboard username>
> password: <contact me via email at natcobbinah1778@gmail.com for admin dashboard password>

> https://multisite-django-app-d49cbac60017.herokuapp.com/en/rosetta
  UI interface to help editing of localization strings for internationalization 


## Running app locally
```
1. Clone app from github

2. cd to app directory and activate the python  virtual environment (.venv)
   > python -m venv .venv
   > .venv/Scripts/activate (on windows)

3. pip install -r requirements.txt

[NOTE]: Since (.env) file containing api-keys and other projects settings is 
added to (.gitignore), you'll need to *manually* create a (.env) file in the 
base root of the cloned project directory, and add the following variables:

   SECRET_KEY= <generate secret key using python shell>
   > python manage.py shell
   > import secrets
   > print(secrets.token_urlsafe())
   > copy secrets and substitute in place of <generate secret key using python shell>

   DATABASE_URL_LOCAL = sqlite:///db.sqlite3
   OPENAI_SECRET_KEY = <contact me via email at natcobbinah1778@gmail.com to send apikey to test chatbot using chatgpt>
   ADMIN_NAME = Nathaniel_Cobbinah
   ADMIN_EMAIL = fmg3ckali@gmail.com

4. python manage.py migrate

5. python manage.py createsuperuser

6. python manage.py runserver

7. append /admin at the end of the browser URL, to login to the admin dashboard,
that is because the (post model) uses a user object property, which after logging in
can be retrieved using (request.user)

7. Navigate and test app features
```

## Sample Screenshots from App Locally Served
Homepage (en)
![blog site homepage 1](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/067530e2-506d-413f-b77d-8fddda4e6dd5)

![blog page homepage 2](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/3a2b9e93-5e2c-4a85-a90e-72f6a6cfd33a)

Homepage (fr)
![blog site hompepage 1 fr](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/68918e12-a4da-4add-9eee-89f5072febae)

Create Post
![create new post](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/71e5b182-9f07-47f3-8559-5e555f445e91)

Read post
![read post in detail](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/469c2208-f847-47fe-b3e1-aa5381343c97)

Edit read post
![edit read post](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/c8eafc7f-5711-4212-a58a-f44074fa5c72)

![alert toast](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/4fd605a7-41d2-4a49-a2c3-c8e549d8e46b)

Searching
Search by post title
![search for post by title](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/014dc766-fcee-493b-a719-bae3c947c93b)

Search by content
![search for post by content](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/76434ddb-83f0-4a0c-8d51-850d3d842d1a)

Chatbot usage
![gpt-integration](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/731f51c1-50e3-48ea-89c6-fe813d39ab8a)

![gpt-chatbot](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/bc343be6-0bef-4c54-91da-b7d1fbfd9c39)

![chatbot players of all time](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/2953f0c5-9e41-4974-9cc5-f690447af2b2)

## Sample Screenshots from App Accessed Remoted hosted on Heroku
![on heroku - post created](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/0762e5c4-7964-4846-85f8-778ed8c91949)

![on heroku - post updated](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/3a9aa6a0-e1f4-4bff-a767-6bad8bd5c4d1)

![on heroku chatbot working successfully](https://github.com/natcobbinah/Django_BlogMultiLingual/assets/10479361/9c085d7c-a9b9-4a70-a1a4-3605d1f7762f)


