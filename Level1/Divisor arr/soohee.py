def solution(arr, divisor):
    answer = [i for i in arr if i%divisor == 0]
    return sorted(answer) if len(answer)>0 else [-1]

print(solution([5,9,7,10],5))