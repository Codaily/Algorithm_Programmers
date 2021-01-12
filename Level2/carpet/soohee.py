def divisor(yellow):
    div = []
    for i in range(1,yellow+1):
        if (yellow % i ==0):
            div.append(i)
    return div
            
def solution(brown, yellow):
    arr = []
    arr = divisor(yellow)
    total = brown + yellow
    flag = 0

    answer = []
    for i in range((int)(len(arr)/2)+1):
        if flag == 1 :
            break
        width = arr[i] + 2
        length = arr[len(arr)-i-1] + 2
        if (width * length == total):
            answer.append(length) 
            answer.append(width)
            flag = 1         
            break 
        
    return answer


# import math
# def solution(brown, yellow):
#     ans=((brown-4)+math.sqrt((brown-4)**2-16*yellow))//4
#     return [ans+2,yellow//ans+2]