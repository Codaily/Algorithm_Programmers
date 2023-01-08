def solution(msg):
    answer = []
    dic = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    w = msg[0]
    i = 0
    while i != len(msg):
        if w in dic:
            if i != len(msg)-1:
                i += 1
            else:
                answer.append(dic.index(w)+1)
                break
            w += msg[i]
        else:
            answer.append(dic.index(w[:-1])+1)
            dic.append(w)
            w = msg[i]
            

    return answer


print(solution("KAKAO"))
