def solution(n, left, right):
    answer = []
    num_array = [i+1 for i in range(n)] 
    for i in range(left,right+1):
        quo, rem = i//n , i%n
        num = 0
        if quo >= rem:
            num = quo + 1
        else: 
            num = num_array[rem]
        answer.append(num)
    return answer

print(solution(4,7,14))
