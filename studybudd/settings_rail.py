from studybudd.settings import *

from decouple import config

SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS=["web-production-8fa9.up.railway.app/"]