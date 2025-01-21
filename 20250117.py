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

# 백준 문제