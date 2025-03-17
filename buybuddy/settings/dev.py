from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-wthq50vs2buq91_em3@l1pc6(tzsp0qb672yn#9fi8872ml(pk"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# https://www.gisinternals.com/query.html?content=filelist&file=release-1930-x64-gdal-3-10-0-mapserver-8-2-2.zip#google_vignette
# https://download.lfd.uci.edu/pythonlibs/archived/GDAL-3.4.3-cp311-cp311-win_amd64.whl

GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal309.dll"
GEOS_LIBRARY_PATH = r"C:\OSGeo4W\bin\geos_c.dll"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")


try:
    from .local import *
except ImportError:
    pass
