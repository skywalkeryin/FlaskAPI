'''
 Created by skywalkeryin on 7/17/19
'''
from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from sqlalchemy.util import namedtuple

from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import SuperAdminScope, is_in_scope

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, password):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired.', error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']
    endpoint = request.endpoint
    allow = is_in_scope(scope, endpoint)
    if not allow:
        raise Forbidden()
    return User(uid, ac_type, scope)

