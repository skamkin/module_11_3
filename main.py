from inspect import getmodule


def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': obj.__dict__,
        'methods': dir(obj),
        'module': getmodule(obj)
    }

class Myclass:
    def __init__(self):
        self.name = 'Myclass'
        self.description = 1
        self.attributes = 50

obj = Myclass()

number_info = introspection_info(obj)
print(number_info)
