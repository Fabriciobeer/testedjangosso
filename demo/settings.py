# """
# Django settings for django_project project.

# For more information on this file, see
# https://docs.djangoproject.com/en/1.8/topics/settings/

# """

# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os
# import netifaces

# # Find out what the IP addresses are at run time
# # This is necessary because otherwise Gunicorn will reject the connections
# def ip_addresses():
#     ip_list = []
#     for interface in netifaces.interfaces():
#         addrs = netifaces.ifaddresses(interface)
#         for x in (netifaces.AF_INET, netifaces.AF_INET6):
#             if x in addrs:
#                 ip_list.append(addrs[x][0]['addr'])
#     return ip_list

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '822de3122037c69e06c153d3f5b2e0c2'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# # Discover our IP address
# ALLOWED_HOSTS = ip_addresses()

# # Application definition

# INSTALLED_APPS = (
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# )

# MIDDLEWARE_CLASSES = (
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
# )

# ROOT_URLCONF = 'django_project.urls'

# SAML_FOLDER = os.path.join(BASE_DIR, 'saml')

# SESSION_ENGINE = 'django.contrib.sessions.backends.file'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [r'/home/django/django_project/templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'django_project.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
# #         'NAME': 'django',
# #         'USER': 'django',
# #         'PASSWORD': 'd52e1d3bdb3dd17564a4b606d872795b',
# #         'HOST': 'localhost',
# #         'PORT': '',
# #     }
# # }


# # Internationalization
# # https://docs.djangoproject.com/en/1.8/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.8/howto/static-files/

# STATIC_URL = '/static/'
# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# # Allow Django from all hosts. This snippet is installed from
# # /var/lib/digitalocean/allow_hosts.py

# import os
# import netifaces

# # Find out what the IP addresses are at run time
# # This is necessary because otherwise Gunicorn will reject the connections
# def ip_addresses():
#     ip_list = []
#     for interface in netifaces.interfaces():
#         addrs = netifaces.ifaddresses(interface)
#         for x in (netifaces.AF_INET, netifaces.AF_INET6):
#             if x in addrs:
#                 ip_list.append(addrs[x][0]['addr'])
#     return ip_list

# # Discover our IP address
# ALLOWED_HOSTS = ip_addresses()

"""
Django settings for demo project.
For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#import netifaces
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0c7216)gs^ne$%3+je20zuo+g0&^6yb@e68qdr!^!r0hmb-6y+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Find out what the IP addresses are at run time
# This is necessary because otherwise Gunicorn will reject the connections
# def ip_addresses():
#     ip_list = []
#     for interface in netifaces.interfaces():
#         addrs = netifaces.ifaddresses(interface)
#         for x in (netifaces.AF_INET, netifaces.AF_INET6):
#             if x in addrs:
#                 ip_list.append(addrs[x][0]['addr'])
#     return ip_list

# # Discover our IP address
# ALLOWED_HOSTS = ip_addresses()

 ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'demo.urls'

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

SAML_FOLDER = os.path.join(BASE_DIR, 'saml')

SESSION_ENGINE = 'django.contrib.sessions.backends.file'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': {
                'django.contrib.auth.context_processors.auth'
            }
        },
    },
]
