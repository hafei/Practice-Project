# 序列化

import pickle

d = dict(name='Bob', age=20, score=88)

p = pickle.dumps(d)
print(p)
#
#
# f = open("dump.txt",'wb')
# pickle.dump(d,f)
# f.close()
#
# f = open("dump.txt",'rb')
# dump = pickle.load(f)
# f.close()
# print(d)



# JSON

import json

s = json.dumps(d)

print(s)

l = json.loads(s)
print(l)

import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)
jsonS = json.dumps(s, default=lambda obj: obj.__dict__)
print(jsonS)


def dict2student(s):
    return Student(s['name'], s['age'], s['score'])


s = json.loads(jsonS, object_hook=dict2student)
print(s)
