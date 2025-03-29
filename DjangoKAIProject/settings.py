# DjangoKAIProject/settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-your-secret-key-here'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ['BaseApp']
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]
ROOT_URLCONF = 'DjangoKAIProject.urls'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
}]
WSGI_APPLICATION = 'DjangoKAIProject.wsgi.application'

# Инициализация SQLAlchemy
from BaseApp.db_session import global_init
global_init(os.path.join(BASE_DIR, 'celebrities.db'))