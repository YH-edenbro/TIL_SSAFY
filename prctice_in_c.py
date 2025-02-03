T = int(input())

for test_case in range(1, T+1):
    profit = 0
    n = int(input())
    a = list(map(int, input().split()))

    if a.index(max(a)) == 0:
        print(f"#{test_case} {profit}")
    