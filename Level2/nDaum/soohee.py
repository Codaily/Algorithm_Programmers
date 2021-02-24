def solution(n):
    n2 = format(n, 'b')  
    num = n + 1
    ndaum = format(num, 'b')
    
    while n2.count('1') != ndaum.count('1'):
        num += 1
        ndaum = format(num, 'b')
    return num

# print(solution(17))
