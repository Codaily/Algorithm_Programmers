def solution(s):
    answer = [len(s)]
    for i in range(1, len(s)//2 +1):
        cnt = 1
        ss = ''
        tmp = s[:i]
        for j in range(i, len(s), i):
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                ss += str(cnt) + tmp if cnt > 1 else tmp
                cnt = 1
                tmp = s[j:i+j]
        ss += str(cnt) + tmp if cnt > 1 else tmp
        answer.append(len(ss))     
    return min(answer)

print(solution("a"))
# ababyyxxxxcdcdcd
# 2abyy2xx3cd