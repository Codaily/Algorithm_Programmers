def solution(numbers):
    answer = []
    for n in numbers:
        compare = n+1
        while format(n ^ compare,'b').count(1) > 2:
            compare += 1
        answer.append(compare)
    return answer

print(solution([2,7]))
