a = [] # 빈 바구니

n, m = map(int, input().split()) # n : 바구니 개수, m : 바꾸는 시도 횟수

for i in range(1,n+1): #바구니 번호 == 공 번호
    a.append(i)

for item in range(m):
    i,j = map(int, input().split()) #서로 바꿀 바구니 번호
    a[j-1], a[i-1] = a[i-1], a[j-1] # i번째 바구니 공과 j번째 바구니 공 교환 (파이썬만 가능한 방법)
    
print(*a)