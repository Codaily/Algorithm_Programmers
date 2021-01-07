def solution(priorities, location):

    answer = 0
    maxP = max(priorities)

    while True:
        frontPop = priorities.pop(0)
        if  frontPop == maxP:
            answer+=1
            if location == 0:
                break
            else:
                location -= 1
            maxP = max(priorities)
        else:
            priorities.append(frontPop)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1 

    return answer