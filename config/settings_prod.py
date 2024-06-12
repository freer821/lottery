from .settings_base import *

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lottery',
        'USER': 'root',
        'PASSWORD': 'Qwer1234@',
        'HOST': 'db',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True
    }
}