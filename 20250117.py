# 백준 문제 2588 곱셈

a = input()
b = input()

for i in range(2,-1,-1) :
    c1 = int(a) * int(b[i])
    print(c1)

print(int(a)*int(b))