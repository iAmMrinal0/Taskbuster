from .base import *

DEBUG = True

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, "fixtures"),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME'  : os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
