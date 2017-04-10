
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.__members__.items())



from hello import Hello

h = Hello()
h.hello()


print(type(h))

# print(type(Hello))

Hello = type('Hello')

print(type(Hello))