'''
 Created by skywalkeryin on 2019/7/21
'''


class Scope:
    # add view function(endpoint) allow access
    allow_api = []
    # add red print name to allow access
    allow_module = []
    # add view function name to remove access
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))
        return self


class UserScope(Scope):
    allow_api = ['get_user']


class AdminScope(Scope):
    allow_api = ['get_user']

    def __init__(self):
        self + UserScope()


class SuperAdminScope(Scope):
    # allow_api = ['v1.get_super_user']
    allow_module = ['v1.user']

    # 链式现加
    def __init__(self):
        self + UserScope()+ AdminScope()

    # 权限相加




a = SuperAdminScope()



def is_in_scope(scope, endpoint):
    # 反射
    # globals
    # endpoint v1.funview => v1.module.funview
    # v1.redname + view_func
    gl = globals()
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]

    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False
