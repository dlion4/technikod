from .base import *
from .ckeditor_conf import CKEDITOR_CONFIGS

LOCAL_APPS = [
    "accounts",
    "category",
    "posts",
    "pages",
    "writer",
    "dashboard",
    "subscriptions"
]
FRAMEWORK_APPS = [
    "ckeditor",
    "ckeditor_uploader",
    "cloudinary_storage",
    "cloudinary",
]


# context

SITE_CONTEXT_PROCESSORS = [
    # context data for apps
    "gmag.context_processor.get_categories",
    # "writer.context.processors.get_profile",
    "dashboard.context_processors.get_dashboard_popular",
    # const data for site
    "gmag.context_processor.sites_context_data",
    # subscription context
    "subscriptions.context_processors.get_subscription_processors",
]

TEMPLATES[0]['OPTIONS']['context_processors'] += SITE_CONTEXT_PROCESSORS


CKEDITOR_UPLOAD_PATH = "uploads/"
INSTALLED_APPS += LOCAL_APPS
INSTALLED_APPS += FRAMEWORK_APPS


# ckeditor conf
CKEDITOR_CONFIGS = CKEDITOR_CONFIGS


# HELP

HELPLINE = "+2545848786198"


# sending emails
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "newsment@info.co.ke"
