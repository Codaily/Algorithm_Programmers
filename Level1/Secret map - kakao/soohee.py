def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        b1 = int(format(i,"b"))
        b2 = int(format(j,"b"))
        answer.append(str(b1+b2).zfill(n))
    
    for i, j in enumerate(answer):
        answer[i] = j.replace('1', '#').replace('2', '#').replace('0', ' ')
    return answer





