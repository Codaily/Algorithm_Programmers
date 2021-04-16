def solution(n):
    answer = []
    sum = 0
    while n > 0:
        n, rest = divmod(n, 3)
        answer.append(rest)

    for i , j in enumerate(reversed(answer)):
        sum += 3**i * j
    return sum
