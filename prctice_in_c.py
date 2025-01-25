T = int(input())

for i in range(T):
    r, s = map(str, input().split())
    a = []

    for char in s:
        a.append(char)

    for j in range(len(a)):
        a[j] = a[j] * int(r)
    
    s= ''.join(a)
    print(s)
