#!/usr/bin/env python
from setuptools import setup
import platform

install_requires = [
    'django >= 1.8',
    'psycopg2',
    'django-grappelli',
    'djangorestframework',
    'dateutils',
    'django-model-utils',
]
dependency_links = []

setup(name='crop',
      version='1.0',
      packages=["crop",],
      include_package_data=True,
      install_requires=install_requires,
      dependency_links = dependency_links
  )
