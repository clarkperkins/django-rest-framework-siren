# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


description = 'Siren hypermedia support for Django REST Framework'
package = 'rest_framework_siren'
install_requires = [
    'PyYAML>=3.10',
]


def get_version():
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    import rest_framework_siren
    return rest_framework_siren.__version__


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


version = get_version()


setup(
    name='djangorestframework-siren',
    version=version,
    url='https://github.com/clarkperkins/django-rest-framework-siren',
    license='Apache',
    description=description,
    author='Clark Perkins',
    author_email='r.clark.perkins@gmail.com',
    packages=find_packages(),
    package_data=get_package_data(package),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
