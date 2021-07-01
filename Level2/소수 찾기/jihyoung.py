from itertools import permutations
def solution(numbers):
    
    per = []
    for i in range(1, len(numbers)+1):
        per += (list(map(''.join, permutations(list(numbers), i))))
    
    prime = set()

    for i in per:
        # 소수 판별
        flag = 0
        for j in range(2, int(int(i)**0.5)+1):
            if int(i) % j == 0:
                flag = 1
                break
        if flag == 0:
            prime.add(int(i))

    length = len(prime)

    if 1 in prime:
        length -= 1

    if 0 in prime:
        length -= 1

    return length

print(solution("7843"))