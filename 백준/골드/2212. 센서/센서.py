# 문제 : https://www.acmicpc.net/problem/2212

n = int(input())
k = int(input())
sensors = list(set(map(int,input().split())))


def solution(n,k,sensors):
    # 집중국이 센서보다 많거나 같으면 0
    if(n <= k):
        return 0
    
    #거리순으로 정렬.
    sensors.sort()

    #센서간의 거리 길이 구하기.
    distances = []

    for i in range(1,len(sensors)):
        distances.append(sensors[i]- sensors[i-1])

    #센서간의 거리를 오름차순으로 정렬.
    distances.sort()

    #이렇게 접근할 생각을 못했다.
    for i in range(k-1):
        distances.pop()

    answer = 0
    for distance in distances:
        answer += distance
    return answer


print(solution(n,k,sensors))
#그리드 문제라 해답을 알고나면 쉽지만.. 문제를 어떻게 유추하냐
# 문제를 읽고 가장 최적의 식을 어떻게 구하는지가 관건..