from itertools import combinations

def solution(orders, course):
    answer = []
    order_list = []

    # list 형태로 변환
    for order in orders:
        order_list.append(list(map(str, order)))

    #print(order_list)

    # 조합들의 출현 횟수 구하기
    for i in course:
        dict = {}
        for order in order_list:
            combination = list(map(''.join, list(combinations(sorted(order), i))))
            #print(combination)
            for combi in combination:
                if combi in dict:
                    dict[combi] += 1
                    continue
                dict[combi] = 1

        print(dict)
        max_val = max(dict.values())
        print(max_val)
        if max_val >= 2:
            for key, value in dict.items():
                if value == max_val:
                    answer.append(key)

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))