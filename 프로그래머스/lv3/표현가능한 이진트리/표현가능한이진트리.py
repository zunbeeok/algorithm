#문제 https://school.programmers.co.kr/learn/courses/30/lessons/150367
def solution(numbers):
    answer = []
    return answer


# x : 2진수의 길이.
# n : 2진트리의 길이.
def get_binary_tree_len(x, n):
    if(x>n-1):
        n*2
        get_binary_tree_len(x,n)
    else:
        return n-1

def to_binary(n):
    return bin(n).replace("0b","")



test = to_binary(10);

test2 = get_binary_tree_len(len(test),2)
# print(len(test)) #4
# print(test2) #3


#2진수로 변화

#포화노드의 수 구하기.
# 2^n -1

#if 2진수가 6자리 2^2
# while True:
#     if(x>n):
#         n*2
#         continue

    
# 1. 2진수로 변화
# 2. 변화된 포화 노드의 수
# 3. 앞에 0만큼 붙여주기
# 4. 해당 값이 노드가 가능한지 체크. (중위 순회)


# #분할 탐색
def division_search(left, right, arr):
    global flag
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    if arr[mid] == '0':
        for i in range(left, mid):
            if arr[i] == '1':
                flag = False
                return
        for i in range(mid + 1, right + 1):
            if arr[i] == '1':
                flag = False
                return
    division_search(left, mid - 1, arr)
    division_search(mid + 1, right, arr)
    
def solution(numbers):
    global flag
    answer = []
    for n in numbers:
        flag = True
        n = bin(n).replace('0b', '')
        index = 1
        node_count = 0
        while True:
            if pow(2, index) - 1 >= len(n):
                node_count = pow(2, index) - 1
                break
            index += 1
        n = list(('0' * (node_count - len(n))) + n)
        division_search(0, len(n) - 1, n)
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer

# f(x) -> 2 ** floor(log(x)+1) -1