N = int(input())
a = list(map(int, input().split()))
v = int(input())
b = 0

for i in range(0,N) :
    if v == a[i] :
        b += 1

print(b)