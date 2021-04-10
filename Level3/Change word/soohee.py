def solution(begin, target, words):

    beginList = list(begin)
    if not target in words:
        return 0

    i = 0
    play = 0
    while "".join(beginList) != target:
        j = words[i]
        cnt = 0
        play += 1
        for k in beginList:
            if k in j :
                cnt += 1
        if cnt == len(begin)-1 :
            beginList = list(j)
            words.pop(words.index(j))
            i = -1 
        i += 1
    return play

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log","cog"]))