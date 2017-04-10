#  IO  Stream
import time

f = open("../files/files.txt", 'r')

print(f.read())
f.close()

with open("../files/files.txt", 'r') as f:
    print(f.read())
    for line in f.readlines():
        print(line)

with open("../7466035.jpeg", 'rb') as img:
    print(img.read())
    img.close()

with open("../files/files.txt", 'w') as files:
    files.write("zhangmeng 2017年04月09日15:02:41 ")
    files.close()
