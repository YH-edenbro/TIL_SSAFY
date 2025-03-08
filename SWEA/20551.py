# 증가하는 사탕 수열

def candy_box(box):
    min_candy = 0
    n = len(box)  # 상자의 개수
    i = n-1
    while i - 1 >= 0:
        if box[i] <= box[i-1]:
            min_candy += 1
            box[i-1] -= 1
            continue
        else: i -= 1
    for i in range(n):
        if box[i] <= 0:
            return -1
    return min_candy

T = int(input())

for tc in range(1, T+1):
    candy = list(map(int, input().split()))
    result = candy_box(candy)

    print(f'#{tc} {result}')