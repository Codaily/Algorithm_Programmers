def solution(n):
    sum = 0
    for i in range(n):
        if n%(i+1) == 0:
            sum+= i+1
    return sum