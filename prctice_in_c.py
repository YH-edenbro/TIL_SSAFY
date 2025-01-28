a, b, v = map(int, input().split())  #낮에는 a미터, 밤에는 -b미터, 나무막대v

start = 0 # 달팽이의 시작점
day = 0

while start >= v :
    start = start + a
    start = start - b
    day = day + 1
    continue

print(day)