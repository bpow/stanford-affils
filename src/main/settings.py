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
from dotenv import load_dotenv
from django.templatetags.static import static


# Set environment variables.
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production.
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret.
SECRET_KEY = "django-insecure-e9^@hkx*@hqh()&qrle@0z5awy$ao_erfzd1)_4s9a_@cz3^tz"

# SECURITY WARNING: Don't run with debug turned on in production.
DEBUG = True

ALLOWED_HOSTS: list[str] = []

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "affiliations",
    "django_admin_logs",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
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

# Database:
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": f'django.db.backends.{os.getenv("AFFILS_DB_ENGINE")}',
        "NAME": os.getenv("AFFILS_DB_NAME"),
        "USER": os.getenv("AFFILS_DB_USER"),
        "PASSWORD": os.getenv("AFFILS_DB_PASSWORD"),
        "HOST": os.getenv("AFFILS_DB_HOST"),
        "PORT": os.getenv("AFFILS_DB_PORT"),
    }
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
STATIC_URL = "static/"

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
