"""
Django settings for teste project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv('.env.dev')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-406#j$ttriko-3(_+rvimi!h)73q3n(wva#3%t&lw&duub4140'
#SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nome_app',
    'bootstrap5',
    'corsheaders',
    'rest_framework',
]


CORS_ORIGIN_WHITELIST = (
    #'http://localhost:5173',
    'http://localhost:1337',
)

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'teste.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'teste.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
       # 'ENGINE': 'django.db.backends.sqlite3',
       # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        #'NAME': 'postgres',
        #'USER': 'masteruser',
        #'PASSWORD': '12345678',
        #'HOST': 'teste-db.czenacwbzgqz.eu-north-1.rds.amazonaws.com',
        #'USER': 'useraws',
        #'PASSWORD': 'Qwerty1234',
        #'HOST': 'dbproj1.cnprtk3bvxit.eu-west-2.rds.amazonaws.com',
        #'PORT': '5432',
        ##"USER": "postgres",
        ##"PASSWORD": "postgres",
        ##"HOST": "db",  # set in docker-compose.yml
        ##"PORT": 5432,  # default postgres port
        #"ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        #"NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        #"USER": os.environ.get("SQL_USER", "user"),
        #"PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        #"HOST": os.environ.get("SQL_HOST", "localhost"),
        #"PORT": os.environ.get("SQL_PORT", "5432"),
	    #'ENGINE': 'django.db.backends.postgresql',
        #'NAME': 'postgres',
        #'USER': 'masteruser',
        #'PASSWORD': '12345678',
        #'HOST': 'teste-db.czenacwbzgqz.eu-north-1.rds.amazonaws.com',
        #'PORT': '5432'

        #'ENGINE': 'django.db.backends.postgresql',
        #'NAME': 'postgres',
        'NAME': "dbproj1_pgres_aws",#os.environ.get("DB_NAME"),
        #'USER': 'masteruser',
        #'PASSWORD': '12345678',
        #'HOST': 'teste-db.czenacwbzgqz.eu-north-1.rds.amazonaws.com',
        'USER': "useraws",  #os.environ.get("DB_USER"),
        'PASSWORD': "Qwerty1234",#os.environ.get("DB_PASSWORD"),
        'HOST': "dbproj1aws.cnprtk3bvxit.eu-west-2.rds.amazonaws", #os.environ.get("HOST_DB"),
        'PORT': 5432, #os.environ.get("HOST_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = BASE_DIR / 'productionfiles'

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
