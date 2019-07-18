'''
 Created by skywalkeryin on 7/15/2019
'''
import datetime

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError


# json serialization
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d')
        return ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder

