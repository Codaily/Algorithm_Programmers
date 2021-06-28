# def solution(dirs):
#     cnt = 0
#     Way = {"U":[0,1], "D":[0,-1], "R":[1,0], "L": [-1,0]}
#     Loc = [0,0]
#     Visited = []
#     for d in dirs:

#         if -5 < Loc[0] < 5 and -5 < Loc[1] < 5:
#             Loc = [Loc[0]+Way[d][0],Loc[1]+Way[d][1]]
#         if Loc not in Visited:
#             Visited.append(Loc)
#             cnt += 1

#     return cnt

def solution(dirs):
    Way = {"U":[0,1], "D":[0,-1], "R":[1,0], "L": [-1,0]}
    Loc = (0,0)
    Next = (0,0)
    Visited = set()
    for d in dirs:
        Next = Loc[0]+Way[d][0], Loc[1]+Way[d][1]
        if -5 <= Next[0] <= 5 and -5 <= Next[1] <= 5:
            Visited.add((Loc, Next))
            Visited.add((Next, Loc))
            Loc = Next
    return len(Visited) // 2

print(solution("LULLLLLLU"))