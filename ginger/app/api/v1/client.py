'''
 Created by skywalkeryin on 7/15/2019
'''
from app.libs.redprint import Redprint

api = Redprint('client')


@api.route('/register')
def create_client():
    pass