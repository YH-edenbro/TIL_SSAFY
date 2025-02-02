<<<<<<< HEAD
a, b, v = map(int, input().split())
start_m = 0
day = 0

while v >= start_m:
    start_m = start_m + a
    start_m = start_m - b
    day = day + 1

print(day)
    
=======
import sys

n = int(sys.stdin.readline())
a = 0 # 사이클 수
str_n = str(n)
new_n = "0"


while int(new_n) != n:
    if 1 < n < 10 :
        str_n = "0" + str_n
        sum_n = int(str_n[0]) + int(str_n[1])
        new_n = str_n[-1] + (str(sum_n))[-1]
        str_n = new_n
        a = a + 1
    elif n > 10 :
        sum_n = int(str_n[0]) + int(str_n[1])
        new_n = str_n[-1] + (str(sum_n))[-1]
        str_n = new_n
        a = a + 1
    elif n == 0:
        a = 1
        break
    elif n == 1:
        a = 60
        break

print(a)
>>>>>>> fa7e5dccc698dac42180e42b916feca1217c8bc9
