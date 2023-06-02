N = int,input()
K = list(map(int, input().split()))

#정렬
K.sort()

cnt = 0
temp = []

#시간복잡도 O(N)
for kngiht in K:
    temp.append(kngiht)  # 시간복잡도 O(1)
    fear = max(temp) #시간복잡도 O(N)
    
    if(fear == len(temp)): #시간복잡도 O(1)
        temp = []
        cnt += 1

print(cnt)


#내가 짠 코드는 몇의 복잡도일까?
# O(N) * (O(N) + O(2))
# 시간복잡도를 낮출수 있는지 고려하기.

##################################################################################

# n = int(input())
# data = list(map(int, input().split()))

# data.sort()

# result = 0 # 총 그룹의 수
# count = 0# 현재 그룹에 포함된 모험가의 수

# for i in data: # 공포도를 낮은 것 부터 하나씩 확인하며
#     count += 1 # 현재 그룹에 해당 모험가를 포함시키기
#     if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
#         result += 1 #총 그룹의 수 증가시키기
#         count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

# print (result) # 총 그룹의 수 출력