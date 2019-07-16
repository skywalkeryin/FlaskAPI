'''
 Created by skywalkeryin on 7/16/2019
'''
from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we make a mistake. o(╥﹏╥)o'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        if headers:
            self.headers = headers
        super(APIException, self).__init__(msg, None)

    def get_headers(self, environ=None):
        """Get a list of headers."""
        if getattr(self, 'headers', None) is not None:
            return self.headers
        return [("Content-Type", "application/json")]

    def get_body(self, environ=None):
        """Get the JSON body."""
        body = dict(error_code=self.error_code,
                    msg=self.msg,
                    request=request.method + ' ' + self.get_url_no_param())
        text = json.dumps(body, ensure_ascii=False)
        return text

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

