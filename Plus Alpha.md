```
enumerate(iterable, start=0)
- iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
- 튜플형식으로 결과값 제공
ex1)

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

"""
0 apple
1 banana
2 cherry
"""
ex2)

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits, 3):
    print(index, fruit)

"""
3 apple
4 banana
5 cherry
"""
```
```
help(모듈)
- 내장 함수 help를 사용해 모듈에 무엇이 들어있는지 확인 가능
- 사실 모듈 공식 문서를 확인하는게 더 좋음
```