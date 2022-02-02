def solution(numbers):
    answer = []
    for i in numbers:
        # 짝수일 경우 + 1한 값
        if i % 2 == 0: 
            binNum = list(bin(i)[2:]) 
            binNum[-1] = "1"
        else:
            binNum = "0"+ bin(i)[2:]   
            where = binNum.rfind("0")
            binNum = list(binNum)
            binNum[where] = '1'
            binNum[where + 1] = '0'

        # 다시 2진수를 10진수로 변환
        minNum = int("".join(binNum), 2)
        answer.append(minNum)


    return answer

numbers = [2,7]

print(solution(numbers))