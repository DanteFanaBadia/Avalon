"""
Django settings for Avalon project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=y)10$c!_734pgj%1^f10#*)1o&%dhmskmg-)8=x6v(du69u%*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ('0.0.0.0', '127.0.0.1', 'devenv.local:8000')

# Application definition

INSTALLED_APPS = [
    # BEGIN 3's Party Library
    'suit',
    # END

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps
    'core'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Avalon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Avalon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': os.environ.get('DB_NAME', 'avalon'),
        'HOST': os.environ.get('DB_HOST', r'.\SQLEXPRESS'),
        'USER': os.environ.get('DB_USER', 'sa'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'password'),
        'PORT': os.environ.get('DB_PORT', ''),
        'OPTIONS': {
            'DRIVER': 'ODBC Driver 13 for SQL Server'
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Avalon',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
    },
    'MENU_OPEN_FIRST_CHILD': True,  # Default True
    'MENU': (
        'sites',
        {'label': 'Modulo Ordenes', 'icon': 'icon-file', 'models': ('core.order', 'core.part',
                                                                    'core.customer', 'core.employee'), },
    ),

    # misc
    'LIST_PER_PAGE': 15
}

