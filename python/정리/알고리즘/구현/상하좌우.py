n = int(input())
x, y = 1, 1  # 초기 좌표 설정.
# S = list(map(str, input().split()))
plans = input().split()

# L, R, U, D 를 index를 맞춰 설정.
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]


# 이동 게획을 하나씩 확인하기
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            # 파이썬은 초기화를 스택을 뚫고 한다. 자바스크립트의 var랑 똑같나 보다.
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 공간 이동
    x, y = nx, ny

print(x, y)
