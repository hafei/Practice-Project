
class Zhangmeng():
    __slots__ = ('name', 'age', 'work', 'action', 'career')

    def __init__(self):
        self.name = 'zhangmeng'
        self.age = 28
        self.career = 'Programmer'

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return 'name is %s' % self.name

    __repr__ = __str__

    def __iter__(self):
        return self


    def __getattr__(self, attr):
        if attr == 'score':
            return 90

    def __call__(self, *args, **kwargs):
        return print('my name is %s'% self.name)

zm = Zhangmeng()

print(zm.__str__())
print(zm.__repr__())
print(zm.score)
zm()
print(callable(Zhangmeng()))   # 判断对象是否可调用



class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a
#
# for item in Fib():
#     print(item)
#
# f = Fib()
#
# print(f[5])