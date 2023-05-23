# 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/64064

from itertools import permutations
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]


##################################################################################################################
# 내가 만든 로직.
# 각 벤아이디 별로 들어올 수 있는 경우의 수를 추출.
# 조합식 구현에 있어 어려움을 겪어 블로그 참고함.

def solution(user_id, banned_id):
    # 각 자리마다 가능한 경우의 수.
    comb = []
    ban_set = []
    # 벤 아아디 목록 만큼 반복
    for ban in banned_id:
        # 벤 아이디 하나당 들어올 수 있는 아이디 경우의 수
        temp = []
        # user아이디 반복문
        for user in user_id:
            # *를 포함한 글자수가 같은 글자시 return true
            if check_char(ban, user):
                # 벤아이디에 올수 있는 user
                temp.append(user)
        # 벤 아이디 별로 올 수 있는 아이디 목록들을 추가.
        comb.append((temp))
    # 조합별 로직 구하는 경우의 수
    print(comb)
    # user_permutation = list(permutations(comb, len(comb)))

    # print(ban_set)
    # return len(ban_set)
    print(list(set([tuple(set(item)) for item in comb])))

    return len(list(set([tuple(set(item)) for item in comb])))


# 반복문을 중첩으로 할떄 특정 반복문 종료가 불가능해 보여 함수로 변환.
def check_char(ban, user):
    # 총 글자 수 비교.
    if (len(ban) == len(user)):
        # 각 글자마다 같은지 비교
        for i in range(len(user)):
            # 글자가 같거나 벤아이디가 * 인 경우. 계속 반복문 동작
            if user[i] == ban[i] or ban[i] == "*":
                # 마지막 글자시에는 return을 True로 던져 ban아이디에 들어올 수 있는 글자인지 확인.
                if (i == (len(user)-1)):
                    return True
            # 벤아이디 목록에 들어오지 못하는 경우.
            else:
                return False

##################################################################################################################


# def check(users, banned_id):
#     for i in range(len(banned_id)):
#         # 글자수 비교. 글자수가 맞지 않을 시 함수 종료.
#         if len(users[i]) != len(banned_id[i]):
#             return False

#         for j in range(len(users[i])):
#             # 벤아이디가 *인 경우 제외.
#             if banned_id[i][j] == "*":
#                 continue
#             # 벤 아이디가 유저아이디와 글자수가 다른경우 *는 제외 종료.
#             if banned_id[i][j] != users[i][j]:
#                 return False
#     return True


# def solution(user_id, banned_id):
#     # 모든 경우의 수 추출.
#     user_permutation = list(permutations(user_id, len(banned_id)))

#     ban_set = []

#     for users in user_permutation:
#         if not check(users, banned_id):
#             continue
#         else:
#             # 벤아이디에 통과하는 경우의 수
#             # users안의 중복을 제거하기 위해 정렬.
#             # print("####################")
#             # print(users)
#             users = set(users)
#             # print(users)
#             # print("####################")

#             # 중복 제거. (조합이기 때문)
#             # not in 적용시 선형으로 돌아간다.
#             if users not in ban_set:
#                 ban_set.append(users)

#     return len(ban_set)


solution(user_id, banned_id)
