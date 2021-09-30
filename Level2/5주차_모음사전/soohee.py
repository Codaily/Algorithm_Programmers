def solution(word):
    answer = 0
    alpha = {"A" : 0 , "E" : 1 , "I" : 2 , "O" : 3 , "U" : 4}
    order = [781, 156, 31, 6, 1]
    for idx , w in enumerate(word):
        answer += order[idx] * alpha[w] + 1
    return answer

print(solution("EIO"))

