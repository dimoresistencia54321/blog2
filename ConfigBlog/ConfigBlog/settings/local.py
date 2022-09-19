
from .settings import *
import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'blog1',
        'USER': 'root',
        'PASSWORD': '635271qwzxAS',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),
)
