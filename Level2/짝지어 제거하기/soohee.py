def solution(s):
    arr = []
    for i in s:
        if len(arr) == 0 : 
            arr.append(i)
        elif arr[-1] == i:
            arr.pop()
        else:
            arr.append(i)

    return 1 if len(arr) == 0 else 0

print(solution("baabaa"))