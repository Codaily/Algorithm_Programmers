def solution(s):
    answer = [len(s)]
    for num in range(1,len(s)//2+1):
        length = len(s)
        cnt = 0
        isContinue = True
        slist =list(map(''.join, zip(*[iter(s)]*num)))
        if slist.count(s[0]) == length:
            return len(str(length)) +1 
        for l , m in zip(slist[:-1],slist[1:]):
            if l == m:
                if not isContinue : length += 1
                length = length - len(l)  
                isContinue = True
                cnt += 1  
            else:
                isContinue = False
        answer.append(length+len(str(cnt)))

    return min(answer)

print(solution("zzzbbabbabba"))