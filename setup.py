import os
import re
from setuptools import setup, find_packages


def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
        return readme.read()


def version():
    pattern = re.compile(r'__version__ = \'([\d\.]+)\'')
    with open(os.path.join('dcf', '__init__.py')) as f:
        data = f.read()
        return re.search(pattern, data).group(1)


setup(
    name='django-celery-flow',
    version=version(),
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    description='A library that integrates celery period tasks in the Django admin portal',
    long_description=readme(),
    url='https://github.com/cipriantarta/django-celery-flow',
    author='Ciprian Tarta',
    author_email='me@cipriantarta.ro',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Framework :: Django",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
    ],
    keywords='django celery beat task periodic flow',
    install_requires=[
        'django>=1.7',
        'six',
    ],
    test_suite='dcf.tests',
)
