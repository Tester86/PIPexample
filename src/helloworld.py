def say_hi(name=None):
    if name is None:
        return "Hello World"
    else:
        return "Hello, {}".format(name)