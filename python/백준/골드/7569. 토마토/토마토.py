# def main():
# 상자 수 입력. 후 int 변환
m, n = map(int, input().split())
box = []
address1 = []
day = 0
D = [(-1, 0), (0, -1), (1, 0), (0, 1)]
# 초기화.
for i in range(n):
    # n
    box.append(list(map(int, input().split())))
    # m
    for j, y in enumerate(box[i]):
        if (y == 1):
            # 1의 위치 추적용.
            address1.append([i, j])
if (len(address1) == 0):
    # print("익은 토마토가 없다.")
    print(1)
# 0일 경우에는 종료.
# 1의 위치를 기반으로 좌우  앞뒤로 확인.
# 1발견시 위 왼 오 아 순으로 0이 있는지 확인.
# 0발견시 address1 temp 배열에 추가, address1 제거 .
# temp배열 address1으로 변경.
while True:
    tmp = []
    # 유효성 검사
    for x, y in address1:
        # i값 추출; x,y로 변환
        # i=[0,2];
        # x,y가 범위 안인지 확인.
        for dx, dy in D:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if (box[nx][ny] == 0):
                    box[nx][ny] = 1
                    tmp.append([nx, ny])
    # 기존 address1은 처리 완료. (중복검사는 하지 않는다.)
    address1 = tmp
    if (len(address1) == 0):
        break
    day += 1
if (day == 0):
    print(0)
# # 프린트 찍는곳.
# print("---------------------------")
# for i in box:
#     for y in i:
#         print(y, end=" ")
#     print()
# print("---------------------------")
print(day)


# print(main())
