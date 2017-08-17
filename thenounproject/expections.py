import six


class TheNounProjectException(Exception):
    message = six.text_type("Unknown error")

    def __init__(self, message=None, status=None, **kwargs):
        self.message = six.text_type(message) if message else self.message
        self.status = status
        super(TheNounProjectException, self).__init__(message, status, **kwargs)

    def __str__(self):
        return self.message


class ConnectionError(TheNounProjectException):
    message = six.text_type("Connection Error")


class NotFound(TheNounProjectException):
    message = six.text_type("Not Found")
