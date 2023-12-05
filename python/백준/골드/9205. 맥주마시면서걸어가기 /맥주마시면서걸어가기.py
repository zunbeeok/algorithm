#문제 https://www.acmicpc.net/problem/9205
from collections import deque
t = int(input())


def bfs():
    q = deque()
    q.append((start_x, start_y))
    while q:
        x,y = q.popleft()
        if abs(x - goal_x) + abs(y - goal_y) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visit[i]:
                nx, ny = store[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append((nx,ny))
                    visit[i] = True
    print('sad')
    return
    

for i in range(t):
    n = int(input())
    start_x,start_y = map(int, input().split())
    store = []
    for _ in range(n):
        store_x, store_y = map(int, input().split())
        store.append((store_x,store_y))
    goal_x, goal_y = map(int, input().split())
    store.append((goal_x,goal_y))
    visit = [False] * n
    bfs()



#뭐가 문제지?


        