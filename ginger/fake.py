'''
 Created by skywalkeryin on 2019/7/20
'''

from app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()

with app.app_context():
    with db.auto_commit():
        # create super user
        user = User()
        user.nickname = 'super'
        user.password = '123456'
        user.email = '1234@gmail.com'
        user.auth = 2
        db.session.add(user)
