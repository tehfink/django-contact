import os

DEPLOY_PATH = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

SECRET_KEY = 'h)%n7stb559-3(6@4j&55rp0maji*@jcwk*xuw#tv8rnn6w%go'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

ROOT_URLCONF = 'basic_demo.urls'

TEMPLATE_DIRS = (
    os.path.join(DEPLOY_PATH, '../templates')
)

INSTALLED_APPS = (
    'contact',
)
