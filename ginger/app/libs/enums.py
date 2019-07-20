'''
 Created by skywalkeryin on 7/15/19
'''

from enum import Enum

class ScopeTypeEnum(Enum):
    AdminScope = 1
    SuperAdminScope = 2


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
