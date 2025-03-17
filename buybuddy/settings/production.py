from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-wthq50vs2buq91_em3@l1pc6(tzsp0qb672yn#9fi8872ml(pk"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["https://buybuddysave.co.za", "http://buybuddysave.co.za", "buybuddysave.co.za", "167.71.130.8"]

CSRF_TRUSTED_ORIGINS = ["https://buybuddysave.co.za", "http://buybuddysave.co.za"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

STATICFILES_DIRS = [
    "/var/www/Backend/buybuddy/static/",
]

STATIC_ROOT = "/var/www/Backend/static/"

MEDIA_ROOT = "/var/www/Backend/media/"

try:
    from .local import *
except ImportError:
    pass
