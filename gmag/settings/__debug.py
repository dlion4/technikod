from .base import *


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles/"

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / "media"


STATICFILES_DIRS = [BASE_DIR/ 'static']



LOCAL_APPS = [
    "accounts",
    "category",
    "posts",
    "pages",
    "writer",
    "dashboard",
    "subscriptions",
    "tokens",
]
FRAMEWORK_APPS = [
    "corsheaders",
    'django_social_share',

    'storages',
    "tinymce",
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


INSTALLED_APPS += LOCAL_APPS
INSTALLED_APPS += FRAMEWORK_APPS




# HELP

HELPLINE = "+254758489861"


# sending emails
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "newsment@info.co.ke"


CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOWED_ORIGINS = [
    "http://lionnist.com",
    "https://lionnist.com",
    # Add other allowed origins here
]

CSRF_TRUSTED_ORIGINS = [
    "http://lionnist.com",
    "https://lionnist.com",
]



# aws setting configurationnnnnnn


from .awss3 import *


TINYMCE_JS_URL = 'https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js'
TINYMCE_COMPRESSOR = False

TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "960px",
    "menubar": "file edit view insert format tools table help",
    "plugins": [
        'advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'preview', 'anchor', 'pagebreak',
        'searchreplace', 'wordcount', 'visualblocks', 'visualchars', 'code', 'fullscreen', 'insertdatetime',
        'media', 'table', 'emoticons', 'template', 'help'
        ],
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    "language": "es_ES",  # To force a specific language instead of the Django current language.
}