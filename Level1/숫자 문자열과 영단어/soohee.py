def solution(s):
    answer = ''
    makeDigit = ''
    dict = { "zero" : '0', "one" : '1', "two" : '2', "three" : '3', "four" : '4', 
             "five" : '5', "six" : '6', "seven" : '7', "eight" : '8', "nine" : '9' }
    for i in s:
        if i.isalpha():
            makeDigit += i
            if makeDigit in dict:
                answer += dict[makeDigit]
                makeDigit = ''
        else:
            answer += i
    return int(answer)
print(solution("one4seveneight"))


# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)
# print(solution("one4seveneight"))