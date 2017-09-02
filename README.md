# The Noun Project

# python-thenounproject

Python wrapper for The Noun Project's API: [TheNounProject API](http://api.thenounproject.com/).

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

##### Collection list

Return’s a list of all collections

Query Parameters:

limit (int) – maximum number of results

offset (int) – number of results to displace or skip over

page (int) – number of results of limit length to displace or skip over

    api.collection.list()

##### Collection get

Returns a single collection

    api.collection.get(4)

##### Collection get by slug

Returns a single collection

    api.collection.get_by_slug("national-park-service")

##### Collection icons

Retrieve information for a given collection.

Query Parameters:
  
limit (int) – maximum number of results

offset (int) – number of results to displace or skip over

page (int) – number of results of limit length to displace or skip over

    api.collection.icons(55)

##### Collection icons by slug

Returns a list of icons associated with a collection

Query Parameters:
  
limit (int) – maximum number of results

offset (int) – number of results to displace or skip over

page (int) – number of results of limit length to displace or skip over

    api.collection.icons_by_slug("bicycle")

### Icon

##### Icon list

Returns a list of icons

Query Parameters:

limit_to_public_domain (int) – limit results to public domain icons only

limit (int) – maximum number of results

offset (int) – number of results to displace or skip over

page (int) – number of results of limit length to displace or skip over

    api.icon.list("fish")

##### Icon get

Returns a single icon

    api.icon.get(15)

##### Icon get by term

Returns a single icon

    api.icon.get_by_term(15)

##### Icon recent uploads

Returns list of most recently uploaded icons

Query Parameters:
 	
limit (int) – maximum number of results

offset (int) – number of results to displace or skip over

page (int) – number of results of limit length to displace or skip over

    api.icon.recent_uploads(15)
