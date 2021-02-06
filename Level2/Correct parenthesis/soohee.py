def solution(s):

    s = s.replace("()","")
    
    if s.count('(') != s.count(')'):
        return False
    elif len(s)== 0 :
        return True
    elif s[0] == ')' or s[-1] =='(':
        return False
    return True

solution(")()(")