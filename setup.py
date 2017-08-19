#!/usr/bin/env python
# coding=utf-8

import uuid
from setuptools import setup, find_packages
from pip.req import parse_requirements

install_requirements = parse_requirements("requirements.txt", session=uuid.uuid1())
requirements = [str(req.req) for req in install_requirements]

setup(
    name="python-thenounproject",
    version="1.0.1a1",
    description="A Python client for the TheNounProject API.",
    license="MIT",
    author="Yakup Adaklı",
    author_email="yakup.adakli@gmail.com",
    url="http://github.com/yakupadakli/python-thenounproject.git",
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    keywords="the noun project library",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.6",
    ],
    zip_safe=True,
)
