'''
 Created by skywalkeryin on 7/15/2019
'''


from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/v1/user/get')
def get_user():
    return 'test user'
