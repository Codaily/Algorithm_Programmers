def solution(s):
    answer = [len(s)]
    for num in range(1,len(s)//2+1):
        cnt = 1
        string = ''
        slist = [s[i:i+num] for i in range(0, len(s), num)]
        for l , m in zip(slist[:-1],slist[1:]):
            if l == m:
                cnt += 1
            else:
                string += (str(cnt) + l) if cnt > 1 else l
                cnt = 1
        if cnt > 1:
            string += str(cnt) + l 
        else:
            string += m
        answer.append(len(string))

    return min(answer)

print(solution("aabbaccc"))
# ababyyxxxxcdcdcd
# 2abyy2xx3cd
