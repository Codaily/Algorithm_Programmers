def solution(absolutes, signs):
    sum = 0
    for i,j in enumerate(absolutes): 
        sum -= j if signs[i] == False else -j
    return sum

print(solution([4,7,12],[True,False,True]))