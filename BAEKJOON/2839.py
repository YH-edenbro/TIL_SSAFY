# 설탕 배달달

N = int(input())  # 봉지는 3킬로, 5킬로가 있음.

ans = 0
while N % 5 != 0:
    if N == 0:
        break
    if N < 0:
        ans = -1
        break
    N -= 3
    ans += 1

if N % 5 == 0:
    ans += N // 5

print(ans)