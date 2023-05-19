# # 상자 수 입력. 후 int 변환
# m, n = map(int, input().split())
# # 토마토 상자
# box = []

# # 익은 토마토가 담기는 주소
# address1 = []
# day = 0

# # 익은 토마토의 영향력 범위.
# D = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# # 토마토 초기화.
# for i in range(n):
#     # n
#     box.append(list(map(int, input().split())))
#     # m
#     for j, y in enumerate(box[i]):
#         if (y == 1):
#             # 1의 위치 추적용.
#             address1.append([i, j])

# # 익은 토마토가 없는 경우.
# if (len(address1) == 0):
#     print(0)


# # temp배열 address1으로 변경.
# while True:
#     tmp = []
#     # 유효성 검사
#     # 큐를 통해 접근해야한다.
#     for x, y in address1:
#         # i값 추출; x,y로 변환
#         # i=[0,2];
#         # x,y가 범위 안인지 확인.

#         # 코딩 테스트시 100문제 중 80문제가 이렇게 나오니 확인.

#         # 익은 토마토 기준 북, 서, 남, 동의 위치 확인.
#         for dx, dy in D:
#             nx = x + dx
#             ny = y + dy

#             # 유효한 박스 범위 안인지 유효성 검사.
#             if 0 <= nx < n and 0 <= ny < m:
#                 # 익지 않은 토마토 일시
#                 if (box[nx][ny] == 0):
#                     # 토마토를 익힌다.
#                     box[nx][ny] = 1
#                     # 익힌 토마토의 주소를 임시 리스트에 추가.
#                     tmp.append([nx, ny])
#     # 이전 익었던 토마토들에 대채.
#     address1 = tmp

#     # 익지 않은 토마토가 존재하지 않을시. break로 while문 탈출.
#     if (len(address1) == 0):
#         break

#     # 하루가 지나간다.
#     day += 1

# # while문을 돌았음에도 0이라는 말은 익힐 수 있는 토마토가 없다.
# if (day == 0):
#     print(-1)

# # # 프린트 찍는곳.
# # print("---------------------------")
# # for i in box:
# #     for y in i:
# #         print(y, end=" ")
# #     print()
# # print("---------------------------")
# print(day)


# # print(main())


# =================================================================================
from collections import deque

# 상자 수 입력. 후 int 변환
m, n = map(int, input().split())
# 토마토 상자
box = []
# 익은 토마토가 담기는 주소
address1 = deque([])

# 익은 토마토의 영향력 범위.
D = [(-1, 0), (0, -1), (1, 0), (0, 1)]


res = 0

# 토마토 초기화.
for i in range(n):
    # n
    box.append(list(map(int, input().split())))
    # m
    for j, y in enumerate(box[i]):
        if (y == 1):
            # 1의 위치 추적용.
            address1.append([i, j])


def main():
    while address1:
        # 유효성 검사
        # 큐를 통해 접근해야한다.

        # 익은 토마토의 주소를 가져온다.
        x, y = address1.popleft()

        # x,y가 box 안인지 확인.
        # 코딩 테스트시 100문제 중 80문제가 이렇게 나오니 확인.
        # 익은 토마토 기준 북, 서, 남, 동의 위치 확인.
        for dx, dy in D:
            nx = x + dx
            ny = y + dy
            # 유효한 박스 범위 안인지 유효성 검사.
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                # 일자를 따로 빼지 않고 +1씩 더하면서 토마토 상자안에 가장 큰수가 처리 일수다.
                box[nx][ny] = box[x][y] + 1
                # 익힌 토마토의 주소를 임시 리스트에 추가.
                address1.append([nx, ny])

    # # 프린트 찍는곳.
    # print("---------------------------")
    # for i in box:
    #     for y in i:
    #         print(y, end=" ")
    #     print()
    # print("---------------------------")


# print(main())
main()
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)
