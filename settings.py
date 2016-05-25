# Django settings for apoio project.
# -*- coding: utf-8 -*-

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ADMINS = (('Rui Tiago', 'chartervu@operamail.com'),)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/apoiofin/apoiofin/fin.sqlite',
    }
}

TIME_ZONE = 'Europe/Lisbon'

LANGUAGE_CODE = 'pt-pt'

LANGUAGES = (
    ('pt-pt', u'Português'),
    #
)

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = '/home/apoiofin/apoiofin/public/site_media/',

MEDIA_URL = '/site_media/'

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = '##################################################'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
     '/home/apoiofin/apoiofin/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',

    'ident',
    'team',
    'budget',
)

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
