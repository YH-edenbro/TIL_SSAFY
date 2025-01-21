# 백준 문제 2588번 곱셈 - 데이터 타입의 전환이 핵심인 문제.

a = input()
b = input()

for i in range(2,-1,-1) :
    c1 = int(a) * int(b[i])
    print(c1)

print(int(a)*int(b))


# 백준 문제 11382번 꼬마 정민 - 기본 문제

a, b, c = map(int, input().split())
print(a + b + c)

# 백준 문제 10171번 고양이 - \를 특수문자로 출력하는 것을 주의하는 문제

print("""\    /\\
 )  ( ')
(  /  )
 \(__)|""")

# 백준 문제 10172번 개 - ', "" 을 출력하는 방법을 묻는 문제

print('''|\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|''')

# 백준 문제 10950번 A + B - 반복문과 입출력을 테스트하는 문제

T = int(input())
for i in range(T) :
    a, b = map(int, input().split())
    print(a + b)

# 백준 문제 8393번 합 - 반복문과 변수에 합을 추가하는 해결방법

n = int(input())
a = 0
for i in range(1,n+1) :
    a = a + i
print(a)

# 백준 문제 1007번 개수 세기 - 개수를 늘리는 방식의 고민

N = int(input())
a = list(map(int, input().split()))
v = int(input())
b = 0

for i in range(0,N) :
    if v == a[i] :
        b += 1

print(b)

# 백준 문제 25304번 영수증

x = int(input())
n = int(input())
t = 0
for i in range(n) :
    a, b = map(int, input().split())
    t += (a * b)
if t == x :
    print("Yes")
else :
    print("No")

# 백준 문제 25314번 코딩은 체육입니다 - 파이썬 기준 굳이 반복문 필요 x

n = int(input())
a = n // 4
print("long " * a + "int")

# 백준 문제 10818번 최소 최대 문제 - min, max 함수 이용

n = int(input())
a = list(map(int, input().split()))
print(min(a), max(a))

# 백준 문제 2525번 오븐 시계 - 시간은 24시까지, 분은 59까지 표기되는 특성을 이용한 문제.

h,m = map(int, input().split())
m_i = int(input())

m_h = (m + m_i) // 60 # 현재 시간의 분 m 과 내가 요리에 필요한 분 m_i의 합

if (h + m_h >= 24) :
    print((h + m_h - 24), (m + m_i - (60 * m_h)))
else :
    print((h + m_h), (m + m_i - (60 * m_h)))

# 백준 문제 2480 주사위 세개 - 조건문과 적절한 함수 사용이 중요한 문제

a, b, c = map(int, input().split())
d = [a, b, c]

if a == b == c : # 같은 눈 세개
    print(10000 + (a * 1000)) 
elif a == b and a != c : # a,b 같은 눈, c는 다른 눈
    print(1000 + (a * 100)) 
elif a == c and a != b : # a,c 같은 눈, b는 다른 눈
    print(1000 + (a * 100))
elif b == c and a != b : # b,c 같은 눈, a는 다른 눈
    print(1000 + (b * 100))
elif a != b and a != c and b != c :
    print(max(d) * 100)

# 백준 문제 15552번 문제 - sys.stdin.readline()을 이용하여 더 빠른 시행

import sys

T = int(sys.stdin.readline())

for i in range(T) :
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

# 백준 문제 11021번 문제 - A + B - 반복문 안에 표현식을 얼마나 잘 작성하는지 테스트

T = int(input())

for i in range(1,T+1) :
    a, b = map(int, input().split())
    c = a + b
    print(f"Case #{i}: {c}")
