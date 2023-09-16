from .__debug import *


# SECURE_SSL_REDIRECT=os.environ.get("SECURE_SSL_REDIRECT")
# SESSION_COOKIE_SECURE=os.environ.get("SESSION_COOKIE_SECURE")
# CSRF_COOKIE_SECURE=os.environ.get("CSRF_COOKIE_SECURE")

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get("DATABASE_NAME"),
#         'USER': os.environ.get("DATABASE_USER"),
#         'PASSWORD': os.environ.get("DATABASE_PASSWORD"),
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}