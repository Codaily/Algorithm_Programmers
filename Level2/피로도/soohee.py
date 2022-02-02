from itertools import permutations

def solution(k, dungeons):
    dungeon = list(permutations(dungeons))
    cnt = []
    maxHP = k
    for dun in dungeon:
        num = 0
        for d in dun:
            if k >= d[0]:
                k -= d[1]
                num += 1
        cnt.append(num)
        k = maxHP
    return max(cnt)


print(solution(80, [[80,20],[50,40],[30,10]]))