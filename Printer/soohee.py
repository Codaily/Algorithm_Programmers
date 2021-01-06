def solution(priorities, location):

    f_loc = []
    loc = [i for i in range(len(priorities))]

    while len(priorities)>0 :
        if priorities[0] == max(priorities): # max 일때
            f_loc.append(loc.pop(0))
            priorities.pop(0)
        else: #max가 아닐때, 다시 priorities 마지막으로 감.
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
        print(f_loc)
    return f_loc.index(location) + 1
