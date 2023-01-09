def solution(n, k):
    answer = 0
    number = 0
    number = tenToN(n ,k)
 

    num_list = number.split('0')
    for num in num_list:
        if num == '' or int(num) == 1 :
            continue
        
        if isPrimeNumber(int(num)):
            answer += 1
    return answer

def isPrimeNumber(n):
    for i in range(2,int(n**(1/2))+1):
        if n % i == 0:
            return False   
    return True



def tenToN(n, q):
    toN = ''

    while n > 0:
        n, mod = divmod(n, q)
        toN += str(mod)

    return toN[::-1] 

print(solution(110011, 10))
