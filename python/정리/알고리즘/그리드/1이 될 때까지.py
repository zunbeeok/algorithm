# # 내가 짠코드
# def sub(N):
#     return N-1

# def divide(N,K):
#     return N/K

# def solution(N,K):
#     global cnt ;

#     if(N==1):
#         return
    
#     if(N % K == 0):
#         N = divide(N,K)
#     else:
#         N =sub(N)
    
#     cnt += 1
#     solution(N,K)

# cnt =0;
# N = 17
# K = 4

# solution(N,K)
# print(cnt)

######################################################################
#나동빈 코드
n, k =  map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    
    result += (n - target)
    n = target

    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
            break
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
