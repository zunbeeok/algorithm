# 문제 : https://www.acmicpc.net/problem/5557
n = int(input())

numbers = list(map(int,input().split()))

dp = []

#초기화
for i in range(len(numbers)-1):
  dp.append([0 for i in range(21)])


for i in range(len(numbers)-1):
  if i == 0:
    dp[i][numbers[i]] = 1
    continue
  #20이하의 숫자이므로 index로 접근
  for j in range(21):

    prev = dp[i-1][j]

    if j-numbers[i] >= 0 :
      dp[i][j-numbers[i]] += prev
    if j+numbers[i] <=20 :
      dp[i][j+numbers[i]] += prev

print(dp[len(numbers)-2][numbers[len(numbers)-1]])