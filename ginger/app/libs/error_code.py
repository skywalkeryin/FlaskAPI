'''
 Created by skywalkeryin on 7/16/2019
'''

from app.libs.error import APIException


class Success(APIException):
    code = 200
    msg = 'OK'
    error_code = 0


class DeleteSuccess(APIException):
    code = 204
    msg = 'delete success'
    error_code = -1

class ParameterException(APIException):
    code = 400
    msg = 'The parameter is valid.'
    error_code = 1000


class AuthFailed(APIException):
    code = 401
    msg = 'Authorization failed'
    error_code = 1005

class Forbidden(APIException):
    code = 403
    msg = "forbidden, not in scope"
    error_code = 1004

class NotFound(APIException):
    code = 404
    msg = 'the resource are not found 0__0...'
    error_code = 1001


class ServerError(APIException):
    code = 500
    msg = 'sorry, we make a mistake. o(╥﹏╥)o'
    error_code = 999

class ClientTypeError(APIException):
    code = 500
    msg = 'The client is invalid.'
    error_code = 1006


