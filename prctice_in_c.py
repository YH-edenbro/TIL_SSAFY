import sys
from collections import deque

n = int(sys.stdin.readline())
card = [] #카드목록

#카드를 순서에 맞춰 번호 매기기
for i in range(1,n+1):
    card.append(i)

card = deque(card)

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())
    

print(*card)