def solution(dartResult):
    score = []
    num = ''
    for i in dartResult:
        if i.isdigit():
            num += i
        elif i == 'S':
            score.append(int(num)**1)
            num = ''
        elif i == 'D':
            score.append(int(num)**2)
            num = ''
        elif i == 'T':
            score.append(int(num)**3)
            num = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1]*=2
        elif i == '#':
            score[-1]*=-1
    return sum(score)
    

    


print(solution('1D2S#10S'))