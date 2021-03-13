def solution(arr):
    answer = [arr[0]]
    tmp = arr[0]
    for i in arr:
        if tmp != i:
            answer.append(i)
            tmp = i
    return answer
