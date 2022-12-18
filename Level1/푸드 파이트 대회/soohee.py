def solution(food):
    answer = ''
    str1 = ''
    for i in range(1,len(food)):
        if food[i] >= 2:
            str1 += str(i) * int(food[i]//2)
    str2 = str1[::-1]
    answer = str1 + '0' + str2
    
    return answer
