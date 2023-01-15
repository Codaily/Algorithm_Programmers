def solution(n, s):
    div = s // n
    
    if div == 0: return [-1]
    
    answer = [div]
    
    while n > 1:
        s -= s // n
        n -= 1
        answer.append(s // n)
    return answer
