T = int(input())

for i in range(1,T+1):
    m = 0 # 연산 횟수
    a, b, n = map(int, input().split())
   

#  a 와 b 모두 성장해야 하기 때문에 작은 수에 수를 더해줘야 연산 횟수를 줄일 수 있음.
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