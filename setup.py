from distutils.core import setup

setup(
    name = 'django-contact',
    version = '0.4',
    url = 'http://github.com/rcoyner/django-contact/',
    author = 'Ryan Coyner',
    author_email = 'rcoyner@gmail.com',
    description = 'Generic contact form application for Django',
    packages = ['contact'],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ],
)
