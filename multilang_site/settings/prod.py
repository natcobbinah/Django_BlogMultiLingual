# custom settings for production environment
from .base import *
from environs import Env

DEBUG = False
env = Env()

DEBUG = True
env.read_env()

# all information will be sent by email to email_list in admins, when a view
# raises an exception
ADMINS = [
    (env.str("ADMIN_NAME"), env.str("ADMIN_EMAIL")),
]
ALLOWED_HOSTS = ["*",]
DATABASES = {
    'default':  env.dj_db_url("DATABASE_URL")
}
