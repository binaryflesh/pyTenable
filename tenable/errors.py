class UnexpectedValueError(Exception):
    '''
    An unexpected value error is thrown whenever the value specified for a
    parameter is outside the bounds of what is expected.  For example, if the
    parameter **a** is expected to have a value of 1, 2, or 3, and it is instead
    passed a value of 0, then it is an unexpected value, and this Exception
    should be thrown by the package.
    '''
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class APIError(Exception):
    '''
    The APIError Exception is a generic Exception for handling responses from
    the API that aren't whats expected.  The APIError Exception iself attempts
    to provide the developer with enough information around the response to
    ascertain what went wrong.

    Attributes:
        code (int):
            The HTTP response code from the offending response.
        response (request.Response):
            This is the Response object that had caused the Exception to fire.
        uuid (str):
            The Request UUID of the request.  This can be used for the purpose
            of tracking the request and the response through the Tenable.io
            infrastructure.  In the case of Non-Tenable.io products, is simply
            an empty string.
    '''
    def __init__(self, r):
        Exception.__init__(self)
        self.response = r
        self.code = r.status_code
        self.uuid = r.headers['X-Request-Uuid'] if 'X-Request-Uuid' in r.headers else ''

    def __str__(self):
        return repr('{}:{} {}'.format(self.uuid, self.code, self.response.body))


class InvalidInputError(APIError):
    '''
    A InvalidInputError is thrown if there is either incomplete or invalid
    information passed to the API.  The HTTP response code generally associated
    to this Exception is 400.

    Attributes:
        code (int):
            The HTTP response code from the offending response.
        response (request.Response):
            This is the Response object that had caused the Exception to fire.
        uuid (str):
            The Request UUID of the request.  This can be used for the purpose
            of tracking the request and the response through the Tenable.io
            infrastructure.  In the case of Non-Tenable.io products, is simply
            an empty string.
    '''
    def __str__(self):
        return repr('{}:{} {}'.format(self.uuid, self.code, self.response.content))


class PermissionError(APIError):
    '''
    A PermissionError Exception is thrown when the request cannot be completed
    because the user performing the request doesn't have sufficient permissions
    to complete the task.  The HTTP response code generally associated to this
    Exception is 403.

    Attributes:
        code (int):
            The HTTP response code from the offending response.
        response (request.Response):
            This is the Response object that had caused the Exception to fire.
        uuid (str):
            The Request UUID of the request.  This can be used for the purpose
            of tracking the request and the response through the Tenable.io
            infrastructure.  In the case of Non-Tenable.io products, is simply
            an empty string.
    '''
    def __str__(self):
        return repr('{}:{} {}'.format(self.uuid, self.code, self.response.content))


class NotFoundError(APIError):
    '''
    A NotFoundError Exception is thrown when the requested object either
    doesn't exist, or cannot be retreived.  The HTTP response code generally
    associated to this Exception is 404.

    Attributes:
        code (int):
            The HTTP response code from the offending response.
        response (request.Response):
            This is the Response object that had caused the Exception to fire.
        uuid (str):
            The Request UUID of the request.  This can be used for the purpose
            of tracking the request and the response through the Tenable.io
            infrastructure.  In the case of Non-Tenable.io products, is simply
            an empty string.
    '''
    def __str__(self):
        return repr('{}:{} {}'.format(self.uuid, self.code, self.response.content))


class ServerError(APIError):
    '''
    A ServerError is thrown when the HTTP request cannot be completed due to a
    server-side issue.  The HTTP response code generally associated to this
    Exception is 500.

    Attributes:
        code (int):
            The HTTP response code from the offending response.
        response (request.Response):
            This is the Response object that had caused the Exception to fire.
        uuid (str):
            The Request UUID of the request.  This can be used for the purpose
            of tracking the request and the response through the Tenable.io
            infrastructure.  In the case of Non-Tenable.io products, is simply
            an empty string.
    '''
    def __str__(self):
        return repr('{}:{} {}'.format(self.uuid, self.code, self.response.content))


class UnknownError(APIError):
    '''
    If the package is unable to determine what categorization the Exception
    should fall under, it will fall back to this Exception type.  We should
    generally not see UnknownError be thrown.

    Attributes:
        code (int):
            The HTTP response code from the offending response.
        response (request.Response):
            This is the Response object that had caused the Exception to fire.
        uuid (str):
            The Request UUID of the request.  This can be used for the purpose
            of tracking the request and the response through the Tenable.io
            infrastructure.  In the case of Non-Tenable.io products, is simply
            an empty string.
    '''
    def __str__(self):
        return repr('{}:{} {}'.format(self.uuid, self.code, self.response.content))