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

# 백준 문제 11022번 문제 A + B - f-string 연습

T = int(input())

for i in range(1, T + 1) :
    a, b = map(int, input().split())
    c = a + b
    print(f"Case #{i}: {a} + {b} = {c}")

# 백준 문제 2439번 문제 별 찍기(2) - 오른쪽 정렬 str.rjust(자릿수)를 이용한 문제.

n = int(input())
a = '*'
for i in range(1, n + 1) :
    b = a * i 
    print(str(b).rjust(n))

# 백준 문제 10952번 문제 A+B(5) - 무한 루프에서 조건을 넣어 break를 걸어주는 방법

while True :
    a, b = map(int, input().split())
    if (a and b) == 0 :
        break
    print(a + b)

# 백준 문제 10951번 문제 A+B(4) - try, except를 쓰는 문제. 

while True :
    try :
        a, b = map(int, input().split())
        print(a + b)
    except :
        break
    
# 백준 10871번 문제 X보다 작은 수 - 반복문안에 조건문과 언패킹을 적절하게 섞어쓰는 문제

n, x = map(int,input().split())
a = list(map(int, input().split()))
b = []

for i in range(n) :
    if a[i] < x :
        b.append(a[i])

print(*b)

# 백준 2562번 문제 최댓값 - max함수를 사용 가능한지, .index()로 인덱스 번호를 찾을 수 있는지 물어보는 문제

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
n6 = int(input())
n7 = int(input())
n8 = int(input())
n9 = int(input())

a = [n1, n2, n3, n4, n5, n6, n7, n8, n9]
ma = max(a)

print(ma)
print(a.index(ma) + 1)

# 백준 10810번 문제 공 넣기 - 사람의 순서와 파이썬의 순서는 다른 점, 마지막 언패킹까지 꼼꼼하게 할 것. 

n, m = map(int, input().split()) # 공과 바구니의 수 : n / 바구니에 공을 넣는 시도 횟수 : m
b = [] # 빈 바구니 

for item in range(n) : #n개 만큼 바구니의 크기 만들기
    b.append(0)

for item in range(m) :
    i, j, k = map(int, input().split()) # i-j번 바구니까지 담기. k번 번호의 공 선정
    c = [] # 빈 바구니에 넣을 공 주머니 리셋
    for item in range((j-i+1)) :
        c.append(k)
    b[i-1:j] = c

print(*b)

# 백준 10813번 문제 공 바꾸기 - 파이썬 기준으로 간단한 방식으로 공을 교환하는 로직을 만들 수 있음.

a = [] # 빈 바구니

n, m = map(int, input().split()) # n : 바구니 개수, m : 바꾸는 시도 횟수

for i in range(1,n+1): #바구니 번호 == 공 번호
    a.append(i)

for item in range(m):
    i,j = map(int, input().split()) #서로 바꿀 바구니 번호
    a[j-1], a[i-1] = a[i-1], a[j-1] # i번째 바구니 공과 j번째 바구니 공 교환 (파이썬만 가능한 방법)
    
print(*a)

# 백준 5597번 문제 과제 안내신 분..? - for과 자료형의 전환을 연습하는 문제.

a = set() # 전체 출석부
b = set() # 제출한 사람

for i in range(1,31) : # 30명의 출석부 생성
    a.add(i)

for i in range (28) : # 과제 제출한 사람들 명단
    n = int(input())
    b.add(n)

c = a - b # 과제를 제출 안한 학생
d = sorted(list(c)) # 과제 제출 안한 학생 리스트화 + 정렬

for i in range(len(d)) : #과제 제출 안한 학생을 번호 빠른 순서로
    print(d[i])

# 백준 3052번 문제 나머지 - 자료형의 특징을 이해하고 활용하는 문제.

a = set() # 나머지 저장용

for i in range(10) :
    n = int(input())
    a.add(n % 42)

print(len(list(a))) #list의 길이 == 서로 다른 나머지의 개수

# 백준 1152번 문제 단어의 개수 - 공백만 입력했을 때를 고려해야하는 문제.

a = input()

b = a.strip()
c = b.split(sep= ' ')

if a == ' ':
    print(0)
else:    
    print(len(c))

# 백준 11720번 문제 숫자의 합 - 형변환을 잘 사용하는지 묻는 문제.

a = int(input())
b = input() #a의 개수만큼 b에 숫자를 적음

total = 0

for num in b:
    total += int(num)

print(total)

# 백준 27866번 문제 문자와 문자열 - 매우 기본적인 문제.

S = input()
i = int(input())

print(S[i-1])

# 백준 1546번 문제 평균 - for문 활용

n = int(input())
score = list(map(int, input().split()))
m = max(score)

for i in range(len(score)):
    score[i] = score[i]/m*100

result = sum(score)/len(score)
print(result) 