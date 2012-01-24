import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid>=1.3a',
    'transaction',
    'mako',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'Paste',
    'PasteDeploy',
    'PasteScript',
    'velruse',
    'sqlalchemy',
    'zope.sqlalchemy',
    ]

tests_require = [
    'WebTest',
    'mock',
    'nose',
    'coverage',
    ]

setup(name='stockpot',
      version='0.0',
      description='stockpot',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require = tests_require,
      test_suite='stockpot',
      install_requires = requires,
      entry_points = """\
      [paste.app_factory]
      main = stockpot:main
      """,
      paster_plugins=['pyramid'],
      )
