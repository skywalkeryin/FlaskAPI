'''
 Created by skywalkeryin on 7/18/19
'''

# How to serialize an object to a dictionary

class Test:
    p1 = 'dd'

    def keys(self):
        return ['p1']

    def __getitem__(self, item):
        return getattr(self, item)


print(dict(Test()))
