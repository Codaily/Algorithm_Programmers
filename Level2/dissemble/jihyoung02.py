# 두번째 시도 : 딕셔너리 이용 (문제에서 주어진대로 hash를 이용함! 효율이 훨씬 좋아졌고 코드도 보기 좋아짐)
def solution(clothes):

    clothes_info = dict()

    for x, y in clothes:
        if y not in clothes_info:
            clothes_info[y] = 1
        else:
            clothes_info[y] += 1

    answer = 0
    for value in clothes_info.values():
        answer *= (value + 1)
        
    return answer -1
