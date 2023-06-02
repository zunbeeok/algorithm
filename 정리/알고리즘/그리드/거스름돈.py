n = 1260
count = 0


array = [500, 100, 50, 10]

for coin in array:
    # // 몫만 구하는 식
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    # %= 좌항을 우항으로 나눈 나머지 값 대입.
    n %= coin

print(count)