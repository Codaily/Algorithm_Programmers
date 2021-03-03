def solution(x, n):
    answer = [ i for i in range(x,x*(n+1),x) ] if x != 0 else [0]*n
    return answer
