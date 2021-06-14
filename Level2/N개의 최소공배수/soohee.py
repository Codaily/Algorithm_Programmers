import math
def solution(arr):
    answer = arr[0]
    for i in arr:
        answer = ( i * answer) // math.gcd(i,answer)
    return answer
print(solution([2,6,8,14]))
# 최소공배수 = 최대공약수 X A X B 