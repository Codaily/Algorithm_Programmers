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
        
  while seller:
        n = seller.pop()
        money = amount.pop() * 100
        while n != '-':
            for k, v in sell.items():
                if n in v:
                    profit = math.ceil(money * 0.9)
                    money -= profit
                    result[n] += profit
                    n = k
                    break
            if money == 0:
                break

    return list(result.values())

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))
