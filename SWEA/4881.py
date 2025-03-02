def dfs(row, total):
    global min_sum

    # 종료 조건 : 모든 행에서 숫자를 한번씩 고른 상태
    if row == N:
        min_sum = min(min_sum, total)
        return
    
    if total >= min_sum:
        return

    for col in range(N):
        if not visited[col]:
            visited[col] = 1
            dfs(row + 1, total + num_arr[row][col])
            visited[col] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N  # 열 방문 여부 체크
    min_sum = 30  # N 최소 3 값 최대 9 N이 최소일 때 배열 합 최대 27

    dfs(0, 0)  # 첫 번째 행부터 탐색 시작

    print(f"#{test_case} {min_sum}")
