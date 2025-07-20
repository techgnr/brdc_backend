import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-zzmudtdwitbsymls!v2d^zp3@b#sy134h9!!i_l8ncsdi!1hk-"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = True

# ALLOWED_HOSTS = ["tsc.tripurasundaricampus.edu.np"]
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "djoser",
    "core",
    "brdc",
    "django_filters",  # ✅ Add this line"
    "django_summernote",  # for blog section
    # "ckeditor_5",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "brdc_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["brdc_backend/templates"],
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

WSGI_APPLICATION = "brdc_backend.wsgi.application"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
}


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tripuras_brdc',
        'USER': 'tripuras_brdc',
        'PASSWORD': 'khadka@2082',
        'HOST':'192.250.235.43',
        'PORT':'3306',
    }
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "core.User"

CORS_ALLOWED_ORIGINS = [
    "https://tripurasundaricampus.edu.np",  # Frontend URL
    "http://localhost:5173",
]

try:
    from .local_settings import *
except ImportError:
    pass

# settings.py

JAZZMIN_SETTINGS = {
    # Basic branding
    "site_title": "TSCS Admin",
    "site_header": "TSCS Admin",
    "site_brand": "TSCS Admin",
    "welcome_sign": "Welcome to Tripura Sundari Campus, Achham",
    "copyright": "© 2025 Tripura Sundari Campus,Achham",
    ## Logo & favicon
    "site_logo": "images/tsc_logo1.png",  # static/images/logo.png
    "login_logo": "images/tsc_logo1.png",
    "login_logo_dark": "images/logo-dark.png",  # optional dark mode logo
    "site_icon": "images/favicon.png",  # optional favicon (32x32 recommended)
    "site_logo_classes": "img-circle",  # CSS class for logo style
    # Search functionality
    "search_model": ["auth.User", "auth.Group"],
    # Avatar
    "user_avatar": None,
    # Top menu
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "email": "gjkkunwar07@gmail.com", "new_window": True},
        {"model": "auth.User"},
        {"app": "books"},
    ],
    # User menu
    "usermenu_links": [
        {"name": "Support and Help", "url": "", "new_window": True},
        {"model": "auth.user"},
    ],
    # Side menu config
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    # Custom links inside app menu
    "custom_links": {
        "books": [
            {
                "name": "Make Messages",
                "url": "make_messages",
                "icon": "fas fa-comments",
                "permissions": ["books.view_book"],
            }
        ]
    },
    # Icon customization (use FontAwesome classes)
    "icons": {
        "auth": "fas fa-user-shield",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "books": "fas fa-book",
        "books.author": "fas fa-pen-nib",
        "books.book": "fas fa-book-open",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    # Related modal support
    "related_modal_active": True,
    # UI Tweaks
    "use_google_fonts_cdn": True,
    "custom_css": "css/admin_custom.css",  # Optional: static/css/admin_custom.css
    "custom_js": "js/admin_custom.js",  # Optional: static/js/admin_custom.js
    "show_ui_builder": False,
    # Change view UI format
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    # Internationalization
    "language_chooser": False,
}

"""'
For timezone here !
"""

TIME_ZONE = "Asia/Kathmandu"
USE_TZ = True  # Required for timezone-aware datetime
