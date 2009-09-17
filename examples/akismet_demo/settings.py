import os

DEPLOY_PATH = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

SECRET_KEY = 'a$9@!r!@#2ug9e&@!^x^*ms96qd5pv&ytor9-!(op&@z6@$o$_'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

ROOT_URLCONF = 'akismet_demo.urls'

TEMPLATE_DIRS = (
    os.path.join(DEPLOY_PATH, '../templates')
)

INSTALLED_APPS = (
    'contact',
)

AKISMET_API_KEY = '' # Your key
