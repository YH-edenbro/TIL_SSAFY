a = [] # 빈 바구니
b = [] # 순서를 역순으로 바꿀 바구니

n, m = map(int, input().split())

for i in range(1,n+1): # 바구니에 순서 매기기
    a.append(i)

for item in range(m) :
    i, j = map(int, input().split())
    for append in range(j-i+1):
        b.append(0) 
    b[:] = a[j:i-2]
    a[i-1,j] = b[:]

print(*a)