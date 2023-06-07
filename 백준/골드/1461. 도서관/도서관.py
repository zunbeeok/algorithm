# 문제 : https://www.acmicpc.net/problem/1461
n,m = map(int,input().split())
book = list(map(int, input().split()))

max_walk = 0 # 제일 멀리 있는 책의 위치

# 음수, 양수 나누기
left = []
right = []
for item in book:
    if item < 0:
        left.append(item)
    elif item > 0:
        right.append(item)
    #가장 멀리있는 책의 위치
    if abs(item) > abs(max_walk):
        max_walk = item

left.sort()
right.sort(reverse = True)
walking=0

# m권을 들고 양수 방향에 책을 모두 제자리에 놔둔다.
for j in range(0, len(right), m):
    # 제일 멀리 있는 책은 무시한다.
    if right[j] != max_walk:
        walking += right[j]

# m권을 들고 음수 방향에 책을 모두 제자리에 놔둔다.
for k in range(0, len(left), m):
    # 제일 멀리 있는 책은 무시한다.
    if left[k] != max_walk:
        # 최소 걸음 수를 계산하기 위해 절대값으로 바꿔 더한다.
        walking += abs(left[k])


# 최소 걸음 수는 책의 제자리 위치와 현재 책의 위치를 왕복하여 계산한다.
walking *= 2
# 제일 멀리 있는 책을 놔둔다.
walking += abs(max_walk)

print(walking)

#그리디 알고리즘은 최적의 방식