'''
 Created by skywalkeryin on 7/15/2019
'''

from flask import jsonify, g

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_super_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    # if not user:
    #     return NotFound()
    # dict()
    return jsonify(user)




@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    # if not user:
    #     return NotFound()
    # dict()
    return jsonify(user)



@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()

