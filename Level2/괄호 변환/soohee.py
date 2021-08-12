def divideUV(w):
    idx = 1
    u, v = w[0], ''
    while u.count(')') != u.count('('):
        u += w[idx]
        idx += 1
    v = w[idx:]
    return u,v

def isCorrect(u):
    arr = []  
    for i in u:
        if i == '(':
            arr.append(i)
        else:
            if not arr:
                return False
            arr.pop()
    return True

def solution(w):
    answer = ''
    if w == '':
        return ''
    u,v = divideUV(w)

    if isCorrect(u):
        return u + solution(v)
    else:
        answer += '(' + solution(v) + ')'
        for i in range(1,len(u)-1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
    return answer

print(solution("()))((()"))