# 쉬운 거스름돈

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    change_list = [0, 0, 0, 0, 0, 0, 0, 0]
    change_cost = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for i in range(8):
        if N >= change_cost[i]:
            change_list[i] = N // change_cost[i]
            N = N % change_cost[i]

    print(f'#{tc}')
    print(*change_list)