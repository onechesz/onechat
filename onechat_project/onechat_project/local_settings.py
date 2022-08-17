import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-m0vnatc5krz^bj5g456_s92z=-4r9t0vsqfzcd+y$8^ay-talv'
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}}
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/'),)
