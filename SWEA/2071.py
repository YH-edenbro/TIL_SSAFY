T = int(input())

for test_case in range(1, T+1):

    a = list(map(int, input().split()))
    b = sum(a) / len(a) # 평균값
    print(f"#{test_case} {round(b)}")