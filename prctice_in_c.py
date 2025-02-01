n = int(input())
a = list(map(int, input().split()))
b = 0


if 1 in a:
    b += 1


for item in a:
    for num in range(2, item):
        if item % num == 0:
            b += 1
            break
        
        
print(n - b)
