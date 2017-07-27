class Base:
    def __init__(self, a):
        self.a = a

    def set_a(self, new_a):
        self.a = new_a


def func(b, data):
    b = Base(data)


b = Base(4)
func(b, 10)
print(b.a)
