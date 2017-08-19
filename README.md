# python-thenounproject

A library that provides a Python interface to [the TheNounProject API](http://api.thenounproject.com/).

## Installation

The easiest way to install the latest version
is by using pip/easy_install to pull it from PyPI:

    pip install python-thenounproject

You may also use Git to clone the repository from
Github and install it manually:

    git clone https://github.com/yakupadakli/python-thenounproject.git
    cd python-thenounproject
    python setup.py install

Python 2.7, 3.3, 3.4 and 3.6, is supported for now.

## Usage

    from thenounproject.api import Api

    api_key = ""
    secret_key = ""

    api = Api(api_key, secret_key)

### Collection

##### Collection get

Retrieve information for a given collection.

    api.collection.get()
