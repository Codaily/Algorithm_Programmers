def solution(expression):
    digit = ''
    answer = []
    dArr = []
    sign = []
    signList = [['+','-','*'],['+','*','-'],['*','-','+'],['*','+','-'],['-','+','*'],['-','*','+']]
    for i in expression:
        if not i.isdigit():
            sign.append(i)
            dArr.append(digit)
            digit = ''
        else:
            digit += i
    dArr.append(digit)


    for sl in signList:
        dCheckList = dArr[:]
        sCheckList = sign[:]
        for s in sl:
            for i in range(len(sCheckList)):
                if s == sCheckList[i] and len(dCheckList) != 1:
                    idx = i - sCheckList[:i+1].count(0)
                    sCheckList[i] = 0
                    dCheckList.insert(idx, str(eval(dCheckList.pop(idx) + s + dCheckList.pop(idx))))
        answer.append(abs(int(dCheckList[0])))
    return max(answer)

print(solution("100-200*300-500+20"))