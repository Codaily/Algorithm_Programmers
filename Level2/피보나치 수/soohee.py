def solution(n):
    f0 = 0
    f1 = 1
    if n > 2:
        for i in range(1,n):
            f0 , f1 = f1 , f0 + f1     
        return f1 % 1234567
    return n % 1234567
print(solution(5))