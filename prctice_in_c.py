n = int(input())
a = []

for i in range(n):
    a.append('*' + ('*' * 2 * i))

while True:
    for item in a:
        print(item.center(2*n))
    for item2 in a[-2::-1]:
        print(item2.center(2*n))
    break



