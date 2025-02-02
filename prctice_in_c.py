a, b, v = map(int, input().split())
start_m = 0
day = 0

while v >= start_m:
    start_m = start_m + a
    start_m = start_m - b
    day = day + 1

print(day)
    