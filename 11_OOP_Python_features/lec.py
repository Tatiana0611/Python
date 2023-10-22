class MyClass:
    A = 42
    """About class"""

    def __init__(self, a, b):
        """self.__doc__ = None"""
        self.a = a
        self.b = b

    def method(self):
        """Documentation"""
        self.__doc__ = None

# help(MyClass)
u_1 = MyClass(3, 4)
print(u_1.method.__doc__)

a = (1, 2, 3)
print(type(sum(a)))
