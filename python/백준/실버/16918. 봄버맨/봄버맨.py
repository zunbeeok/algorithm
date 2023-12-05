import sys


def all_zero(x, y):
    return [[0 for _ in range(x)] for _ in range(y)]


def boom(map):
    y = len(map)
    x = len(map[0])
    temp = all_zero(len())
    for i in range(y):
        for j in range(x):
            if map[i][j] == 0:
                temp[i][j] = "."
                for di, dj in D:
                    ni = i + di
                    nj = y + dj

                    if 0 <= ni < y and 0 <= nj < x:
                        temp[ni][nj] = "."
    return temp


D = [(-1, 0), (0, -1), (1, 0), (0, 1)]


x, y, n = map(int, input().rstrip().split())

map = []
for _ in range(x):
    map.append(list(input().rstrip()))

status = 1

if n == 1:
    print(map)
    sys.exit

if n % 2 == 0:
    print(all_zero(x,y))
if n% 3 == 0:
    if status == 1:
        print()
