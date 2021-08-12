def solution(dartResult):
    score = []
    num = ''
    dict = {'S':1 , 'D':2 , 'T':3}
    for i in dartResult:
        if i.isdigit():
            num += i
        elif i in dict:
            score.append(int(num)**dict[i])
            num = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1]*=2
        elif i == '#':
            score[-1]*=-1
    return sum(score)
    
print(solution('1D2S#10S'))