'''
 Created by skywalkeryin on 7/15/2019
'''

from flask import Blueprint

from app.api.v1 import book, user, client, token


def create_blueprint():
    bp_v1 = Blueprint('v1', __name__)
    book.api.register(bp_v1)
    user.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)

    return bp_v1
