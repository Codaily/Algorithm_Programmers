def solution(price, money, count):
    result = money - (price * (count * (count + 1) // 2) )
    if result > 0:
        return 0
    return abs(result)
