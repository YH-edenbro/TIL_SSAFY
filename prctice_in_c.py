n, m = map(int, input().split()) # 공과 바구니의 수 : n / 바구니에 공을 넣는 시도 횟수 : m
b = [] # 빈 바구니 

for item in range(n) :
    b.append(0)

for a in range(m) :
    i, j, k = map(int, input().split()) # i-j번 바구니까지 담기. k번 번호의 공 선정
    c = [] # 빈 바구니에 넣을 공 주머니 리셋셋
    for item in range(m) :
        c.append(k)
    b[i:j+1] = c

print(b)
