import sys

n = sys.stdin.readline()

a = []

for i in range(int(n)):
    num = sys.stdin.readline()
    a.append(int(num))

a.sort()
a = set(a)
a = list(a)

for num in a:
    print(num)