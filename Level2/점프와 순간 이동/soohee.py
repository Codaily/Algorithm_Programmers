def solution(n):
    cnt = 0
    
    while n > 0:
        if n % 2 != 0: # 홀수
            n -= 1
            cnt += 1
        n //= 2 # 홀 짝 공통
    
    return cnt

print(solution(5000))