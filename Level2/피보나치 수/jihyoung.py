def solution(n):
    arr = [0, 1]
    next = 0
    for i in range(2, n+1):
        next = arr[i-2] + arr[i-1]
        arr.append(next)

    return arr[-1] % 1234567

n = 5

print(solution(n))

# https://programmers.co.kr/questions/11991