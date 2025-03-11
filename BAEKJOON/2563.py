# 100 x 100 정사각형 모양의 흰색 도화지
paper = [[0] * 100 for _ in range(100)]
N = int(input())  # N: 색종이의 수, 색종이 크기는 10x10 고정
for _ in range(N):
    dl, db = map(int, input().split())  # dl: 색종이 왼쪽 변과 도화지 왼쪽 변 거리, db: 아래 변 사이의 거리 - 인덱스로 활용
    i = 99 - db
    j = dl
    while True:
        paper[i][j] = 1
        j += 1
        if j == dl + 10:
            i -= 1
            j = dl

        if i == 99 - db - 10:
            break
cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1

print(cnt)