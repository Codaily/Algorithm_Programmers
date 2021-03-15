def solution(n, m):
    answer = []
    for i in range(1,n+1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
    return [max(answer),n*m//max(answer)]
    
# from math import gcd
# def solution(n, m):
#     return [gcd(n,m),n*m//gcd(n,m)]

print(solution(3,12))