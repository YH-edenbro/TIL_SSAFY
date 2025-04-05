def dfs(index, start):
    global min_result

    if index == N:
        return

    if len(start) == N // 2:
        link = []
        for link_n in sl:
            if link_n not in start:
                link.append(link_n)

        start_hap, link_hap = 0, 0
        for i in range(N//2 - 1):
            for j in range(i, N//2):
                if i != j:
                    start_hap += (S[start[i]][start[j]] + S[start[j]][start[i]])
                    link_hap += (S[link[i]][link[j]] + S[link[j]][link[i]])
        min_result = min(min_result, abs(start_hap - link_hap))
        return


    # index를 스타트로 선택
    selected[index] = 1
    start.append(sl[index])
    dfs(index + 1, start)
    selected[index] = 0

    start.pop()
    # index를 스타트로 선택x
    dfs(index + 1, start)


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

sl = list(range(N))
selected = [0] * N
min_result = 1000
dfs(0, [])

print(min_result)