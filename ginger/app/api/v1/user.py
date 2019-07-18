'''
 Created by skywalkeryin on 7/15/2019
'''
from flask import jsonify

from app.libs.error_code import NotFound
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

api = Redprint('user')


class Qiyue:
    name = 'yin'
    age = 18

    def keys(self):
        return ['name', 'age']

    def __getitem__(self, item):
        return getattr(self, item)


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    # if not user:
    #     return NotFound()
    # dict()
    return jsonify(user)
