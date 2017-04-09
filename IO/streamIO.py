# 内存读写

from io import StringIO

f = StringIO()

f.write("Hello")

print(f.getvalue())

from io import BytesIO

b = BytesIO()

b.write('中文'.encode('utf-8'))

print(b.getvalue())
