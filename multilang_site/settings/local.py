# custom settings for local environment
from .base import *
from environs import Env
env = Env()

DEBUG = True
env.read_env()
DATABASES = {
    "default": env.dj_db_url("DATABASE_URL_LOCAL")
}
