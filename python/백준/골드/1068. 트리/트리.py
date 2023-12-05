#문제 : https://www.acmicpc.net/problem/1068
N = int(input())
tree = list(map(int, input().split())) #[-1, 0, 0, 1, 1] tree의 index는 자기 자신의 번호 , tree의 value는 부모 노드 번호
erase = int(input()) # 1

#-2로 지운다.
def dfs(v):
    #자기 자신 삭제.
    tree[v] = -2
    #자식 노드 삭제.
    for i in range(len(tree)):
        if tree[i] == v:
            dfs(i)
            
dfs(erase)

cnt = 0
for i in range(len(tree)):
    if tree[i] != -2 and i not in tree:
        cnt +=1

print(cnt)    
