import os.path
import io
import sys

from setuptools import setup

# This check is to make sure we checkout docs/_themes before running sdist
if not os.path.exists("./docs/_themes/README"):
    print('Please make sure you have docs/_themes checked out while running setup.py!')
    if os.path.exists('.git'):
        print('You seem to be using a git checkout, please execute the following commands to get the docs/_themes directory:')
        print(' - git submodule init')
        print(' - git submodule update')
    else:
        print('You seem to be using a release. Please use the release tarball from PyPI instead of the archive from GitHub')
    sys.exit(1)


here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.rst')) as f:
    readme = f.read()

setup(
    name='flask-oidc-keycloak',
    description='OpenID Connect extension for Flask - Keycloak',
    long_description=readme,
    long_description_content_type='text/x-rst',
    url='https://github.com/vucanews/flask-oidc-keycloak',
    author='Erica Ehrhardt, Patrick Uiterwijk, Lars Wilhelmsen, Tyler Banks',
    author_email='tyler@vucanews.com',
    version='0.6.2',
    packages=[
        'flask_oidc_keycloak',
    ],
    install_requires=[
        'Flask',
        'itsdangerous',
        'oauth2client',
        'six',
        'python-jwt',
        'jwcrypto',
        'cachetools'
    ],
    extras_require={
      'dev': [
        'twine',
        'tox',
        'bumpversion',
        'nose',
        'nosy'
      ]
    },
    tests_require=['nose', 'mock'],
    entry_points={
        'console_scripts': ['oidc-register=flask_oidc_keycloak.registration_util:main'],
    },
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
