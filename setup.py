#!/usr/bin/env python

from setuptools import setup

setup(name='singer-target-stitch',
      version='2.0.6',
      description='Singer.io target for the Stitch API',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['target_stitch'],
      install_requires=[
          'jsonschema==2.6.0',
          'mock==2.0.0',
        #   removed because of pip dependency issues
        #   'requests==2.20.0',
        #   'singer-python==5.8.0',
          'psutil==5.3.1',
          'simplejson==3.11.1',
          'aiohttp==3.5.4',
        #   'cchardet==2.1.4',
          'aiodns==2.0.0',
	  'ciso8601',
      ],
      extras_require={
          'dev': [
              'nose==1.3.7',
              'astroid==2.1.0',
              'pylint==2.1.1'
          ]
      },
      entry_points='''
          [console_scripts]
          singer-target-stitch=target_stitch:main
      ''',
      packages=['target_stitch'],
)
