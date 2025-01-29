n, m = map(int, input().split())

a = []

for item in range(1,n+1):
    a.append(item)

for item in range(m):
    i, j = map(int, input().split())
    a[i-1:j] = a[j-1:i+1:-1]

print(*a)