def solution(x, y, n):
    answer = 0
    sets = set()
    sets.add(x)
    while sets:
        if y in sets:
            return answer
        next = set()
        for i in sets:
            if i+n <= y:
                next.add(i+n)
            if i*2 <= y:
                next.add(i*2)
            if i*3 <= y:
                next.add(i*3)
        sets = next
        answer+=1

    return -1
