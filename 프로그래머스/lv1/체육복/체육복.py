#왜 그리드 알고리즘인지 생각해보기.
#오름차 순으로 정렬하면  j에 index를 따로 주어서도 더 시간 복잡도를 줄일 수 있다?

def solution(n, lost, reserve):
    # answer = 0
    success = 0
    
    #정렬
    lost.sort()
    reserve.sort()
    
    #여분체육복을 가지고 있지만 도둑 맞아 빌려줄수 없는친구.
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if(reserve[j] == lost[i]):
                lost[i] = -1 #자기 자신의 체육복을 사용하니 -1로 변경.
                reserve[j] =-1
                success+=1

 
    # print(reserve)
    for i in range(len(lost)):
        dx = lost[i] - 1
        dy = lost[i] + 1
        
        #여분 체육복을 가져왔지만 도둑 맞은 경우 제외.
        if(i == -1):
            continue;
        
        for j in range(len(reserve)):
            if(reserve[j] == dx):
                reserve[j] = -1
                success += 1
                break
            if(reserve[j] == dy):
                reserve[j] = -1
                success += 1
                break

    answer = n - len(lost) + success
    return answer



#테스트는 통과했지만 시간복잡도도 구리고 코드도 구린것 같다.
# 반번호가 올라가면 해당 번호 아래만큼은 돌아갈 필요가 없다. 30줄 range 를 시작 지점을 따로 지정하는것도 좋아보인다.

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.4MB)
# 테스트 6 〉	통과 (0.01ms, 10MB)
# 테스트 7 〉	통과 (0.14ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.01ms, 10.3MB)
# 테스트 10 〉	통과 (0.04ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.01ms, 10.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 9.99MB)
# 테스트 16 〉	통과 (0.01ms, 10.4MB)
# 테스트 17 〉	통과 (0.01ms, 10.3MB)
# 테스트 18 〉	통과 (0.01ms, 10.3MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.1MB)
# 테스트 21 〉	통과 (0.00ms, 10.1MB)
# 테스트 22 〉	통과 (0.01ms, 10.2MB)
# 테스트 23 〉	통과 (0.01ms, 10.3MB)
# 테스트 24 〉	통과 (0.03ms, 10.4MB)
# 테스트 25 〉	통과 (0.01ms, 10.3MB)