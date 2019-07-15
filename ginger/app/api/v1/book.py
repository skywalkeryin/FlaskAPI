'''
 Created by skywalkeryin on 7/15/2019
'''

from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('/v1/user/get')
def get_book():
    return 'test'
