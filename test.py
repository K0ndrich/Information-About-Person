class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):

        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError(
                "Недопустимое имя атрибута")
        else:
            print("__SETATTR__")
        # object.__setattr__(self, key, value)
        self.__dict__[key] = value

    def __getattr__(self, item):
        print("__GETATTRIBUTE")
        return False

    def __delattr__(self, item):
        print("__delattr__")
        object.__delattr__(self, item)


a = Point(5, 3)

del a.x
print(a.__dict__)
