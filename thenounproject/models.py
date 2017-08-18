from thenounproject import expections


class ResultSet(list):
    """A list like object that holds results from a  API query."""


class Model(object):
    _not_found_error_class = expections.NotFound

    def __init__(self, **kwargs):
        self._repr_values = {"id": "ID"}

    @classmethod
    def parse(cls, data, sub_item=False):
        data = data or {}
        if not data and not sub_item:
            raise cls._not_found_error_class()
        instance = cls() if data else None
        for key, value in data.items():
            if type(value) == str:
                value = value.strip()
            setattr(instance, key, value)
        return instance

    @classmethod
    def parse_list(cls, data):
        results = ResultSet()
        data = data or []
        for obj in data:
            if obj:
                results.append(cls.parse(obj))
        return results

    def __repr__(self):
        items = filter(lambda x: x[0] in self._repr_values.keys(), vars(self).items())
        state = ['%s: %s' % (self._repr_values[k], repr(v)) for (k, v) in items]
        return '<%s: %s >' % (self.__class__.__name__, ', '.join(state))


class Collection(Model):

    def __init__(self, **kwargs):
        super(Collection, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "slug": "Slug"}

    @classmethod
    def parse(cls, data, sub_item=False):
        collection = super(Collection, cls).parse(data, sub_item=sub_item)
        if hasattr(collection, "author"):
            collection.author = Author.parse(collection.author, sub_item=True)
        return collection


class Author(Model):

    def __init__(self, **kwargs):
        super(Author, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}


class Icon(Model):

    def __init__(self, **kwargs):
        super(Icon, self).__init__(**kwargs)
        self._repr_values = {"id": "Id", "attribution": "Attribution"}

    @classmethod
    def parse(cls, data, sub_item=False):
        icon = super(Icon, cls).parse(data, sub_item=sub_item)
        if hasattr(icon, "uploader"):
            icon.uploader = Author.parse(icon.uploader, sub_item=True)
        return icon


class Uploader(Model):

    def __init__(self, **kwargs):
        super(Uploader, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "username": "Username"}


class Usage(Model):

    def __init__(self, **kwargs):
        super(Usage, self).__init__(**kwargs)
        self._repr_values = {"daily": "Daily", "hourly": "Hourly", "monthly": "Monthly"}

    @classmethod
    def parse(cls, data, sub_item=False):
        usage = super(Usage, cls).parse(data, sub_item=sub_item)
        if hasattr(usage, "limits"):
            usage.limits = Limit.parse(usage.limits, sub_item=True)
        return usage


class Limit(Model):

    def __init__(self, **kwargs):
        super(Limit, self).__init__(**kwargs)
        self._repr_values = {"daily": "Daily", "hourly": "Hourly", "monthly": "Monthly"}
