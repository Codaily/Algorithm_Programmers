import math
def solution(n,a,b):
    answer = 0
    for i in range(int(math.log2(n))):
        if a == b:
            return answer
        else:
            a , b = math.ceil(a/2), math.ceil(b/2)
            answer += 1
    return answer

print(solution(8,1,2))