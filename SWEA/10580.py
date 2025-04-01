T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 전선의 개수
    line_lst = []
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        line_lst.append((Ai, Bi))
    cnt = 0
    i = 0
    while i < N:
        for j in range(1, N):
            if i + j < N:
                if (line_lst[i][0] > line_lst[i+j][0] and line_lst[i][1] < line_lst[i+j][1]):
                    cnt += 1
                elif (line_lst[i][1] > line_lst[i+j][1] and line_lst[i][0] < line_lst[i+j][0]):
                    cnt += 1
            else:
                break
        i += 1

    print(f'#{tc} {cnt}')

    # 전봇대