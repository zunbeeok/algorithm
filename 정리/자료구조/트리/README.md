# 트리


## 트리란?
트리는 가계도와 같은 계층적인 구조를 표현할때 사용할 수 있는 자료구조

* 루트 노드 : 부모가 없는 최상위 노드
* 단말 노드 : 자식이 없는 노드
* 크기 : 트리에 포함된 모든 노드의 개수
* 깊이 : 루트 노드부터의 거리
* 높이 : 깊이 중 최대값
* 차수 : 각 노드의 (자식 방향) 간선 개수

기본적으로 트리의 크기가 N일 때, 전체 간선의 개수는 N - 1개 입니다.


## 이진 탐색 트리

이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조의 일종입니다.
이진 탐색 트리의 특징: 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자신 노드
* 부모 노드보다 왼쪽 자식 노드가 작습니다.
* 부모 노드보다 오른쪽 자식 노드가 큽니다.

```
if 이진 탐색트리가 이미 구성되어 있다고 가정시 값을 찾는법. 

목표값(N) : 37

* step1 : 루트 노드부터 시작하며 루트 노드보다 목표값이 클시 오른쪽을 선택.
* step2 : 현재 노드와 값을 비교하여 작을시 왼쪽, 클시 오른쪽을 선택.
* step3 : 이 과정을 통해 목표 값이다.

이진 탐색트리는 이진탐색이 가능한 형태로 탐색을 수행할 수 있도록 고안된 트리 자료구조의 일종.
```
O(log n)의 복잡도를 가진다.

## 트리의 순회
트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법을 의미.

대표적인 트리 순회방법.
* 전위 순회 : 루트를 먼저 방문한다.
* 중위 순회 : 왼쪽 자식을 방문한 뒤에 루트를 방문
* 후위 순회 : 오른쪽 자식을 방문한 뒤에 루트를 방문

## 파이썬에서 트리의 순회.

```
class Node:
    def _init_( self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node= right_node

# 전위 순회
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])

# 후위 순회
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')

n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None" :
        left_node = None
    if right_node == "None" :
        right_node = Node
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
```