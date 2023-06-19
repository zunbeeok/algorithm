# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    que = deque()
    que.append((begin, 0))
    
    while que:
        word, count = que.popleft()

        for i in range(len(words)):
            if word == target:
                return count

            if check(word, words[i]):
                #큐에추가
                que.append((words[i],count+1))

#글자수 체크용
def check (x, y):
    cnt = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            cnt += 1
    
    return cnt == len(x)-1 
        