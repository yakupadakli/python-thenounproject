from thenounproject import expections


class ResultSet(list):
    """A list like object that holds results from a  API query."""


class Model(object):
    not_found_error_class = expections.NotFound

    def __init__(self, **kwargs):
        self._repr_values = {"id": "ID"}

    @classmethod
    def parse(cls, data, sub_item=False):
        data = data or {}
        if not data and not sub_item:
            raise cls.not_found_error_class()
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
