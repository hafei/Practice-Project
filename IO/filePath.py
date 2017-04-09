import os

print(os.name)

print(os.uname())

print(os.environ)

print(os.path.abspath("."))

print(os.path)

print([x for x in os.listdir('.') if os.path.isdir(x)])

print(os.listdir('.'))

print(os.path.pardir)

# 父级目录
print(os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)))

print(os.path.abspath(os.path.dirname("__file__")))

from datetime import datetime

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
