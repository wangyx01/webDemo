#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from os import path
from setuptools import setup, find_packages
from pkg_resources import yield_lines

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt')) as f:
    install_requires = list(yield_lines(f.read()))


setup(
    packages=find_packages(
        include=('website*',)
    ),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
    python_requires='~=3.6',
    # entry_points={
    #     'paste.app_factory': [
    #         'main = lico.proxy.filesystem.factory:create_host_app',
    #         'container = lico.proxy.filesystem.factory:create_container_app'
    #     ]
    # }
)
