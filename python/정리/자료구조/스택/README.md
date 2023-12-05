# 스택

## 스택이란?
* 먼저 들어온 데이터가 나중에 나가는 형식(선입선출)의 자료구조입니다.
* 입구와 출구가 동일한 형태로 스택을 시각화할 수 있습니다.

## 스택 구현 예시
```
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.append(2)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) #최하단 원소부터 출력