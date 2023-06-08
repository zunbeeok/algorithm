# # 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/67259
# from collections import deque



# def solution(board):
#     arrays=[]
#     n = len(board)
#     # costBoard = [[ [maxsize] * N for _ in range(n) ] for _ in range(4)]

#     #상, 하, 좌, 우
#     D = [(-1,0), (0,1), (1,0), (0,-1)]

#     queue = deque()
#     queue.append((0,0,100,0,[]))
#     while queue:
#             x, y, cost, i, point = queue.popleft()

#             for dx, dy in D:
#                 board[x][y] = 1
#                 nx = x + dx
#                 ny = y + dy
                
#                 #벽이거나 범위 안이지 체크
#                 if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
#                     continue

#                 #직선인지 코너인지 체크
#                 if(len(point)<=2):
#                     px,py =0,0
#                 else: 
#                     px,py = point[i-2]

#                 if(dx != px and dy != py):
#                     ncost = cost + 500
#                 else :
#                     ncost = cost +100
#                     #코너일시 500원
#                 if(nx == n-1 and ny == n-1):
#                     arrays.append(cost)
#                 i+=1
#                 point
#                 #append 
#                 queue.append((nx,ny,ncost,(x,y)))
#     arrays.sort()

#     return arrays[0]


# solution([[0,0,0],[0,0,0],[0,0,0]])



################################################################
from collections import deque


def solution(board):
    size = len(board[0])
    visit = [[-1] * size for _ in range(size)]
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # y,x 위, 오른쪽, 아래, 왼쪽
    result = []

    def bfs():
        q = deque([[0, 0, 0, (0, 0)]])
        while q:
            y, x, cost, od = q.popleft()
            ody , odx = od
            for dy, dx in d:
                ny = y + dy
                nx = x + dx                                                                                                                                              
                money = 100 if (dx == odx and dy == ody) or cost == 0 else 600  # 전과 같은 방향이거나 시작 +100 / 코너 +600
                ncost = cost + money
                if (
                    (0 <= ny < size and 0 <= nx < size)  # 경계
                    and board[ny][nx] == 0  # 벽 아님
                    and (visit[ny][nx] == -1 or visit[ny][nx] >= ncost)  # 처음오거나 더 좋은 비용의 길
                ):
                    visit[ny][nx] = ncost
                    q.append([ny, nx, ncost, (dy,dx)])

    bfs()
    return visit[-1][-1]

#스터디 이후에 추가로 작성하기.



