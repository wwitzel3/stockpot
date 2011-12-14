import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'transaction',
    'mako',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'pymongo',
    'Ming',
    'Paste',
    'PasteDeploy',
    'PasteScript',
    'velruse',
    ]

tests_require = [
    'WebTest',
    'mock',
    ]

setup(name='ccb',
      version='0.0',
      description='ccb',
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
      test_suite='ccb',
      install_requires = requires,
      entry_points = """\
      [paste.app_factory]
      main = ccb:main
      """,
      paster_plugins=['pyramid'],
      )
