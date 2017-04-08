from types import MethodType


class Student(object):
    # __slots__ = ('name', 'age', 'score','set_age')  #__slots__变量，来限制该class实例能添加的属性   动态添加

# @property装饰器就是负责把一个方法变成属性调用的
    def __init__(self):
        self.score = 0

    @property
    def say(self):
        return 'Hello world'

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        self._score = value


s = Student()

s.name = 'Mac'


def set_age(self, age):
    self.age = age
    # self.test = test


s.set_age = MethodType(set_age, s)

s.set_age(25)

print(s.age)
s.score = 80
print(s.score)
print(s.say)
# Student.set_age = set_age



