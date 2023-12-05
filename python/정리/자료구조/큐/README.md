# 큐 자료구조

## 큐 란?
* 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조입니다.
* 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있습니다.


## 큐 구현 예시
* list 자료형으로도 큐를 구현 할 수 있지만 시간 복잡도가 높다.
* 파이썬에서는 deque 라이브러리를 사용한다.
```
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.resverse() # 역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력
```