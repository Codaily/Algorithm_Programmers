from collections import Counter


def solution(want, number, discount):
    day = 0
    dict = {}
    for i in range(len(want)):
        dict[want[i]] = number[i]
    
    for idx in range(len(discount)-9):   
        c = Counter(discount[idx:idx+10])
        if c == dict:
            day += 1

    return day
