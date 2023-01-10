def solution(arrayA, arrayB):
    answer = 0
    gcd1 = makeGcd(arrayA)
    gcd2 = makeGcd(arrayB)
    
    if cannotDiv(arrayA, gcd2):
        if answer < gcd2:
            answer = gcd2
    
    if cannotDiv(arrayB, gcd1):
        if answer < gcd1:
            answer = gcd1

    return answer


def cannotDiv(arr, f):
    for a in arr:
        if a % f == 0:
            return False      
    return True

def makeGcd(arr):
    num = arr[0]
    for i in range(1,len(arr)):
        num = gcd(num, arr[i])
    return num

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a


print(solution([10,20], [5, 17, 20] ))
