"""Django settings.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see:
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see:
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

# Built-in libraries:
from pathlib import Path
import os

# Third-party dependencies:
from dotenv import load_dotenv, find_dotenv
from django.templatetags.static import static
import boto3

# Set environment variables.
load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production.
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: Don't run with debug turned on in production.
DEBUG = False

ALLOWED_HOSTS = ["affils.clinicalgenome.org", "affils-test.clinicalgenome.org"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3001",
]

CSRF_TRUSTED_ORIGINS = [
    "https://affils.clinicalgenome.org",
    "https://affils-test.clinicalgenome.org",
]

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "rest_framework",
    "affiliations",
    "django_admin_logs",
    "django_extensions",
    "dbbackup",  # django-dbbackup
    "django_crontab",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [f"{BASE_DIR}/affiliations/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"
ASGI_APPLICATION = "main.asgi.application"

# Database:
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": f'django.db.backends.{os.environ.get("AFFILS_DB_ENGINE")}',
        "NAME": os.environ.get("AFFILS_DB_NAME"),
        "USER": os.environ.get("AFFILS_DB_USER"),
        "PASSWORD": os.environ.get("AFFILS_DB_PASSWORD"),
        "HOST": os.environ.get("AFFILS_DB_HOST"),
        "PORT": os.environ.get("AFFILS_DB_PORT"),
        "ATOMIC_REQUESTS": True,
    }
}

STORAGES = {
    "dbbackup": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "bucket_name": os.environ.get("AFFILS_AWS_S3_BUCKET_NAME"),
            "access_key": os.environ.get("AFFILS_AWS_ACCESS_KEY"),
            "secret_key": os.environ.get("AFFILS_AWS_SECRET_KEY"),
            "region_name": os.environ.get("AFFILS_AWS_REGION"),
            "default_acl": os.environ.get("AFFILS_AWS_S3_ACL"),
        },
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Password validation:
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization:
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images):
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = "/static/"

STATICFILES_DIRS = [BASE_DIR / "affiliations" / "static"]

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "/media/"

# Default primary key field type:
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "affiliations.renderers.BrowsableAPIRendererWithoutForms",
    ),
}

UNFOLD = {
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/png",
            "href": lambda request: static("images/favicon-32x32.png"),
        },
    ],
    "COLORS": {
        "primary": {
            "100": "210 227 247",
            "200": "197 222 252",
            "300": "121 180 252",
            "400": "121 180 252",
            "500": "51 121 183",
            "600": "23 162 184",
            "700": "30 81 131",
            "800": "22 55 96",
            "900": "22 55 96",
            "950": "22 55 96",
        },
    },
}

# django-admin-logs

# By default, Django creates log entries with the message “No fields changed”
# when an unchanged object is saved in the admin interface. The below prevents
# such log entries from being created.

DJANGO_ADMIN_LOGS_IGNORE_UNCHANGED = True

CRONJOBS = [
    # Run dbbackup weekly on Sundays at midnight
    ("0 0 * * 0", "django.core.management.call_command", ["dbbackup"]),
]

# Logging and Cloudwatch
logger_boto3_session = boto3.client(
    "logs",
    aws_access_key_id=os.environ.get("AFFILS_AWS_ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("AFFILS_AWS_SECRET_KEY"),
    region_name=os.environ.get("AFFILS_AWS_REGION"),
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["watchtower"]},
    "formatters": {
        "aws": {
            "format": "%(asctime)s [%(levelname)-8s] %(message)s [%(pathname)s:%(lineno)d]",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "watchtower": {
            "level": "INFO",
            "class": "watchtower.CloudWatchLogHandler",
            "boto3_client": logger_boto3_session,
            "log_group_name": "Affiliation_Logs",
            # Different stream for each environment
            "stream_name": f"affiliation-{os.environ.get('AFFILS_ENV')}-logs",
            "formatter": "aws",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "aws",
        },
    },
    "loggers": {
        # Use this logger to send data just to Cloudwatch
        "watchtower": {
            "level": "INFO",
            "handlers": ["watchtower"],
            "propagate": False,
        }
    },
}
