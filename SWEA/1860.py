T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # N : 붕어빵 예약 손님 수, M : K개의 붕어빵을 만들기 위한 초 K : 붕어빵 개수
    arrive_s = list(map(int, input().split()))
    arrive_s.sort()

    max_arrive_s = max(arrive_s)
    can_make = [0] * (max_arrive_s + 1)

    i = M
    while i < max_arrive_s + 1:
        can_make[i] += K
        i += M
    result = "Possible"
    cnt = 0
    for num in arrive_s:
        for i in range(num+1):
            if can_make[i] != 0:
                can_make[i] -= 1
                cnt += 1
                break  # for i
    if cnt != N:
        result = "Impossible"

    print(f"#{tc} {result}")