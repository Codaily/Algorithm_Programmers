from collections import Counter


def solution(s):
    answer_int = []
    answer = []
    s =(s.replace('{','').replace(',',' ').split('}'))[:-2]
    s1 = [i.split() for i in s]
    s2 = sorted(s1, key=lambda x:len(x))
    for slist in s2:
        for i in slist:
            if i not in answer:
                answer.append(i)
                answer_int.append(int(i))
                break
    return answer_int
