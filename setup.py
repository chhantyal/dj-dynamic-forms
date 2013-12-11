#!/usr/bin/env python
import os
import codecs
from setuptools import setup


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


from dynamic_forms import get_version


setup(
    name='dj-dynamic-forms',
    version=get_version(),
    description='Dynamic forms for Django - data storage in Postgres Hstore. It is a reusable Django application to create and configure forms through the admin.',
    long_description=read('README.rst'),
    author='Nar Kumar Chhantyal',
    author_email='nkchhantyal@gmail.com',
    url='http://github.com/chhantyal/dj-dynamic-forms',
    license='BSD',
    packages=[
        'dynamic_forms',
        'dynamic_forms.migrations',
    ],
    package_data = {
        'dynamic_forms': [
            'locale/*/LC_MESSAGES/*',
            'templates/dynamic_forms/*',
        ]
    },
    install_requires=[
        'Django>=1.5',
        'django-appconf>=0.6',
        'six',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Framework :: Django',
    ],
    zip_safe=False
)
