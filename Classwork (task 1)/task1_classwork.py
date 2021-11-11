from os import path
from timeit import timeit
from random import randint

f = open("file_integers.txt", "w")
while (path.getsize('file_integers.txt') / 1000000) < 50:
    f.write(str(randint(0, 10000)) + "\n")

s = """
file1 = open("file_integers.txt", "r")
res = 0
for line in file1.readlines():
    if line.strip().isdigit():
        res+=1
file1.close()
"""
print(timeit(s, number=10))

s = """
file2 = open("file_integers.txt", "r")
res = 0
for line in file2:
    if line.strip().isdigit():
        res+=1
file2.close()
"""
print(timeit(s, number=10))

s = """
file3 = open("file_integers.txt", "r")
res = sum(int(line.strip().isdigit()) for line in file3)
file3.close()
"""

print(timeit(s, number=10))

# 17.075724100000002
# 14.58740689999999
# 17.81590159999999
