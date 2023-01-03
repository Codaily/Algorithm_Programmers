
def solution(number, limit, power):
    answer = 1
    for i in range(2,number+1):
        num = getDivisorCount(i)
        if num > limit:
            answer += power        
        else:
            answer += num
    
    return answer

def getDivisorCount(number):

    count = 0
    for i in range(1, int(number**(1/2))+1): 
        if number%i == 0:
            if i == number//i: 
                count += 1
            else:
                count += 2 
    return count

print(solution(10,3,2))
