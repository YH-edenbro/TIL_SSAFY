T = int(input())

for i in range(1,T+1):
    m = 0 # 연산 횟수
    a, b, n = map(int, input().split())
   
    while True:
        if a > b:
            b += a
            m += 1
            if b > n:
                break
        else:
            a += b
            m += 1
            if a > n:
                break

    print(m)