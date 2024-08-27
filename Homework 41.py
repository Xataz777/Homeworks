import inspect


def introspection_info(obj):
    res = {}
    res['type'] = type(obj)
    res['attributes'] = obj.__dict__
    res['methods'] = dir(obj)
    res['module'] = inspect.getmodule(obj)
    print(res)


class MyClass:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def plus(self):
        self.number += 1

    def minus(self):
        self.number -= 1


obj1 = MyClass('AAA', 4)

introspection_info(obj1)
