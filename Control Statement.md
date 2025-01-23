# 제어문(Control Statement)

- 코드의 실행 흐름을 제어하는 데 사용되는 구문.
- 조건에 따라 코드 블록을 싱행하거나 반복적으로 코드를 실행.

## 제어문의 종류

- **조건문**

    - if, elif, else

- **반복문**

    - for, while
- **반복문 제어**

    - break, continue, pass

### 조건문(Conditional Statement)
- 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀.

```
if / elif / else
- 파이썬 조건문에 사용되는 키워드
```

- 복수 조건문

    - 조건식을 동시에 검사하는 것이 아니라 "순차적"으로 비교

- 중첩 조건문

    - 조건문 안에 조건문

### 반복문(Loop Statement)

- 주어진 코드 블록을 여러 번 반복해서 실행하는 구문

```
for                       
특정 작업을 반복적으로 수행

while
주어진 조건이 참인 동안 반복해서 실행

- 파이썬 반복문에 사용되는 키워드
```

```
-for statment의 기본 구조-

for 변수 in 반복 가능한 객체 :
    코드 블록
```
- 반복 가능한 객체(iterable) : 반복문에서 순회할 수 있는 객체(시퀀스 객체 뿐만 아니라 dict, set 등도 포함)

    - dict, set는 순서가 없는데요?
    
        -> 출력하는데 순서는 보장되기 때문에 

### for 문 작동원리

- 리스트 내 첫 항목이 반복 변수에 할당되고 코드블록이 실행
- 다음으로 반복 변수에 리스트의 2번쨰 항목이 할당되고 코드블록이 다시 실행
- ... 마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 싱행

```
items = ['apple', 'banana', 'coconut']

for item(단수형 변수명) in items(복수형 변수명):

appple
banana
coconut
```

```
- 문자열 순회

country = 'Korea'

for char in country:
    print(char)

K
o
r
e
a
```

```
- range 순회

for i in range(5):
    print(1)

0
1
2
3
4
```
```
-딕셔너리 순회(key출력이 기본본)

my_dict = {
    'x' : 10,
    'y' : 20,
    'z' : 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])
x
10
y
20
z
30
```

```
-인덱스로 리스트 순회

numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2


print(numbers)  # [8, 12, 20, -16, 10]
```

### while 문 작동원리

- 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행
 
    == 조건식이 거짓(False)가 될 때 까지 번복

```
while 조건식:
    코드 블록
```

### 적절한 반복문 활용하기

- for

    - 반복 횟수가 명확하게 정해져 있는 경우에 유용
    - 예를 들어 리시트, 튜플, 문자열 등과 같은 시퀀스 형태의 데이터를 처리 할 때

- while

    - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
    - 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

### 반복 제어
- for문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만 때때로 일부만 실행하는 것이 필요할 때가 있음

- break

    - 반복을 즉시 중지
- continue

    - 다음 반복으로 건너뜀
- pass

    - 아무런 동작도 수행하지 않고 넘어감
---
**플래그 변수** : 기준이 되는 변수(ex: 짝수를 찾았는지)

### List Comprehension 
- 간결하고 효율적인 리스트 생성 방법
- 단점 : 가독성이 떨어짐.(비권장, 남용x)

```
[표현식 for 변수 in iterable]

list(표현식 for 변수 in iterable)
```
```
[표현식 for 변수 in iterable if 조건식]

list(표현식 for 변수 in iterable if 조건식)
```
