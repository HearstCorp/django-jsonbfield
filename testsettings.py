SECRET_KEY = 'secret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'HOST': 'localhost',
        'USERNAME': 'db_user',
        'PASSWORD': 'db_pass'
    }
}

INSTALLED_APPS = (
    'jsonbfield',
)
