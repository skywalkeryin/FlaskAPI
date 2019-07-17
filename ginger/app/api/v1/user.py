'''
 Created by skywalkeryin on 7/15/2019
'''
from app.libs.error_code import NotFound
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    # if not user:
    #     return NotFound()
    return 'test user'
