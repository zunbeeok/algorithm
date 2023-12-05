n = int(input())
customer = [0]+list(map(int, input().split()))
m = int(input())


dp = [[0] * (n+1) for _ in range(4)]

for i in range(4):
    for j in range(1, n+1):
        if i == 0:
            dp[i][j] = dp[i][j-1] + customer[j]
