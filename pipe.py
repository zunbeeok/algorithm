# 문제
# https://www.acmicpc.net/problem/17070

# 참고 사이트
# dp에 대해 설명
# https://velog.io/@eunseokim/BOJ-17070%EB%B2%88-%ED%8C%8C%EC%9D%B4%ED%94%84-%EC%98%AE%EA%B8%B0%EA%B8%B0-1-dp-%ED%92%80%EC%9D%B4-python

# 수학공식으로 설명
# https://rebas.kr/838

# dps 참고 블록
# https://backtony.github.io/algorithm/2021-03-02-algorithm-boj-class4-44/


# 재귀로 문제를 접근한다면? dfs?
# 가로일때 경우의 수
# 세로일때 경우의 수
# 대각선일때 경우의 수
################################################################################################

################################################################################################
def dfs(pos):
    global cnt
    x, y, z = pos

    # n,n 도달
    if x == n - 1 and y == n - 1:
        cnt += 1
        return

    # 가로 세로 대각선의 경우 대각선 이동
    if x + 1 < n and y + 1 < n:
        if graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
            dfs((x + 1, y + 1, 2))

    # 가로 대각선의 경우 가로 이동
    if z == 0 or z == 2:
        if y + 1 < n:
            if graph[x][y + 1] == 0:
                dfs((x, y + 1, 0))

    # 세로 대각선의 경우 세로 이동
    if z == 1 or z == 2:
        if x + 1 < n:
            if graph[x + 1][y] == 0:
                dfs((x + 1, y, 1))


n = int(input())
graph = [[] for _ in range(n)]
cnt = 0
# 그래프 정보 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))

# x,y,현재방향
dfs((0, 1, 0))

print(cnt)
