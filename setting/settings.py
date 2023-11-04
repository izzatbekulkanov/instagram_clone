from datetime import timedelta
from pathlib import Path
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config('SECRET_KEY')

# EMAIL_HOST = config('EMAIL_HOST', default='localhost')
# EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [

    # Theme
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',

    # packages
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'phonenumbers',
    'twilio',


    # local APP
    'users',
    'post',
    'shared',
]
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        "rest_framework.permissions.IsAuthenticated", ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'setting.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config("DB_NAME"),
        'USER': config("USER"),
        'PASSWORD': config("PASSWORD"),
        'HOST': config("HOST"),
        "PORT": config("PORT")
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Jazzmin Full example
JAZZMIN_SETTINGS = {
    "site_title": "Kutubxonaga Admin",
    "site_header": "Jazzmin",
    "site_brand": "Kutubxona",
    "site_logo": "images/ulkanov.png",
    "login_logo": "images/ulkanov.png",
    "login_logo_dark": "images/ulkanov.png",
    "site_logo_classes": "img-circle",
    "site_icon": "images/ulkanov.png",
    "welcome_sign": "Jazzminga xush kelibsiz",
    "copyright": "Izzatbek Ulkanov",
    "search_model": ["auth.User", "auth.Group"],
    "user_avatar": None,

    ############
    # Yuqori Menyu #
    ############

    # Yuqori menyuga qo'shiladigan havolalar
    "topmenu_links": [

        # Qayta qilinadigan URL (huquqlar qo'shish mumkin)
        {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},

        # yangi oyna ochadigan tashqi URL (huquqlar qo'shish mumkin)
        {"name": "Yordam", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # model adminni ulashish uchun (modelga huquqlar qo'shish mumkin)
        {"model": "auth.User"},

        # Appning dropdown menyusi bo'lgan barcha model sahifalari uchun (modelga huquqlar qo'shish mumkin)
        {"app": "books"},
    ],

    #############
    # Foydalanuvchi Menyusi #
    #############
    "usermenu_links": [
        {"name": "Yordam", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.users"}
    ],

    #############
    # Yon Menyu #
    #############

    # Yon menyuning ko'rsatiladimi yoki yo'qmi
    "show_sidebar": True,

    # Menyuning avtomatik kengayishi yoki yo'qmi
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    "custom_links": {
        "books": [{
            "name": "Xabarlar yaratish",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.users": "fas fa-users",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Bog'liq Modal #
    #################
    # Popup o'rniga modal ishlatish
    "related_modal_active": False,

    #############
    # UI O'zgartirishlar #
    #############
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    # Yuqori panjara o'zgartiruvchisini yon menyuda ko'rsatish
    "show_ui_builder": False,

    ###############
    # O'zgartirishni ko'rsatish #
    ###############
    "changeform_format": "horizontal_tabs",
    # modeladmin asosida o'zgartirish shaklini o'zgartirish
    "changeform_format_overrides": {"auth.users": "collapsible", "auth.group": "vertical_tabs"},
    # Ma'muriyatni saytning ichki tilini o'zgartirish uchun tarjima bo'limi qo'shish
    "language_chooser": False,
}
