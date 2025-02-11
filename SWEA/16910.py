# 원 안의 점

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = 0

    for num1 in range(-N,N+1):
        for num2 in range(-N,N+1):
            if num1**2 + num2**2 <= N**2:
                a +=1

    print(f"#{tc} {a}")