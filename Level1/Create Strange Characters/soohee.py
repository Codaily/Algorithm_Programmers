def solution(s):
    s = list(s)
    num = 0
    for i,j in enumerate(s):
        if j == ' ':
            num = i+1
        if (i-num)%2 == 0:
           s[i] = j.upper()
        else:
            s[i] = j.lower()
    return ''.join(s)
