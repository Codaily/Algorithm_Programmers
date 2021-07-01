from itertools import permutations
import math
def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    arr = set()
    for i in range(1,len(numbers)+1):
        nlist = list(map(''.join, permutations(numbers, i)))
        for n in nlist:
            arr.add(int(n))
    
    for a in arr:
        if a < 2:
            continue
        else:
            if isPrime(a): 
                answer += 1
    return answer

print(solution("7843"))

