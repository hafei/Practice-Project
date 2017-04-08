std1 = {'name': 'zhangsan', 'score': 88}
std2 = {'name': 'lisi', 'score': 90}


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


bart = Student('Bart Simpson', 88)
lisa = Student('Lisa Simpson', 90)


# bart.print_score()
# lisa.print_score()



# inherit


class Animal(object):
    def run(self):
        print('Animal is Running.....')


class Dog(Animal):
    def run(self):
        print('Dog is Running.....')

    def eat(self):
        print('Dog eating')


class Cat(Animal):
    def run(self):
        print('Cat is Running')


dog = Dog()

# dog.run()
# dog.eat()
#
# print(isinstance(dog, Animal))
#

def run_twice(animal):
    animal.run()
    animal.run()


# run_twice(Dog())


import types


print(type(Animal))
print(type(dog))

def fn():
    pass

print (type(fn)==types.FunctionType)


# for item in dir(Animal):
#     print(item)



