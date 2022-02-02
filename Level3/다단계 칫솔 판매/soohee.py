import math
def solution(enroll, referral, seller, amount):
    result = {}
    sell = {}
    for idx, name in enumerate(referral):
        if name not in sell:
            sell[name] = [enroll[idx]]
        else:
            sell[name] += [enroll[idx]]
        result[name] = 0
    print(sell) 

    # visited = []
    # while seller:
    #     n = seller.pop()
    #     money = amount.pop() * 100

    #     for k, v in sell.items():
    #         if n in v:
    #             profit = math.ceil(money * 0.9)
    #             money -= profit
    #             result[n] += profit
    #             n = k

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))
