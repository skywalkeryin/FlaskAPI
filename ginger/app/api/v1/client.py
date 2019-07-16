'''
 Created by skywalkeryin on 7/15/2019
'''
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 注册　
    # 网页　客户端
    #
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    # else:
    #     raise ClientTypeError()

    # exceptions
    # 可以预知的异常， APIException
    # 未知异常
    # AOP thinking
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
