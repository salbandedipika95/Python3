#python program to get a dictionary from an object's fields
class A(object):
    def __init__(self):
        self.A=1
        self.B=2
obj=A()
print(obj.__dict__)