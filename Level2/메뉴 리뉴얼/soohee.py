from itertools import combinations
def solution(orders, course):
    answer = set()
    menu = []
    menuSet = set()
    dict = {}

    for ord in orders: # menu 조합 만들기
        for co in course:
            menu = list(combinations(ord,co))
            for m in menu:
                menuSet.add("".join(m))


    for m in menuSet: # 주문된 메뉴 세트 확인
        for ord in orders:
            cnt = 0
            for i in m:
                if i in ord:
                    cnt+= 1
            if cnt == len(m):
                if m not in dict:
                    dict[m] = cnt//len(m)
                else: dict[m] += 1
    
    dict = sorted(dict.items(), key= lambda x: x[1] , reverse=True)
    for co in course:
        maxCount = 0
        for d in dict:
            if len(d[0]) == co and maxCount <= d[1] :  
                maxCount = d[1]     
                if maxCount > 1:  
                    answer.add(d[0])
            elif maxCount > d[1]:
                break

    return sorted(answer)

print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
#print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))