# DFS 메서드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
        
# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8], # 1번노드의 인접 노드
    [1, 7], #2번 노드의 인접 노드
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9 #graph는 0~8까지 총 9개의len을 가지고 있는 2차원 배열이기 때문에 0을 포함한 9를 곱해준다.


dfs(graph, 1, visited)

# 배열의 index와 viseited를 맞춰주는게 조금 더 직관적이기 때문에 좋다.
