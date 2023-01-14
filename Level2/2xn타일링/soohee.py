def solution(n):
    mod = 1000000007
    b = [0 for _ in range(n+1)]
    b[0] = b[1] = 1
    b[2] = 2
    
    for i in range(3, n+1):
        b[i] = (b[i-1] + b[i-2]) % mod
    
    return b[n]
