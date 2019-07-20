'''
 Created by skywalkeryin on 2019/7/21
'''


class SuperAdminScope:
    allow_api = ['v1.get_super_user']



class AdminScope:
    allow_api = ['get_user']


def is_in_scope(scope, endpoint):
    # 反射
    # globals
    gl = globals()
    scope = globals()[scope]()
    return endpoint in scope.allow_api
