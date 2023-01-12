def solution(n, t, m, p):
    answer = '0'
    for num in range(1, t*m):
        number = n 
        string = ""
        while num != 0:
            num, mod = divmod(num, number)

            if number > 10 and (10 <= mod) and (mod <= 15):
                string += "ABCDEF"[mod%10]
            else:
                string += str(mod)
        
        answer += string[::-1]

    answerArr = []
    for i in range(p-1, t*m, m):
        answerArr.append(answer[i])
 
    return "".join(answerArr)
